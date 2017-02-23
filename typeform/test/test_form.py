from unittest import TestCase

import requests_mock

from typeform import Form
from typeform import (
    InvalidRequestException, NotAuthorizedException, NotFoundException,
    RateLimitException, UnknownException
)
from . import fixtures


class FormTestCase(TestCase):
    def test_form_get_responses(self):
        """
        When requesting the responses for a form
            we get the responses we expect
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', json=fixtures.FORM_RESPONSE_200)
            responses = form.get_responses()

            # Assert we made the correct request
            self.assertEqual(m.call_count, 1)
            last_request = m.last_request
            self.assertDictEqual(last_request.qs, dict(
                key=['test_api_key'],
            ))

        self.assertEqual(len(responses), 1)
        self.assertEqual(len(responses.responses), 1)
        self.assertEqual(len(responses.questions), 2)

        question_by_id = dict((q.id, q) for q in responses.questions)

        self.assertEqual(question_by_id['email_id'].id, 'email_id')
        self.assertEqual(question_by_id['email_id'].field_id, 1234)
        self.assertEqual(question_by_id['email_id'].question, 'What is your email address?')

        self.assertEqual(question_by_id['list_id_choice'].id, 'list_id_choice')
        self.assertEqual(question_by_id['list_id_choice'].field_id, 56789)
        self.assertEqual(question_by_id['list_id_choice'].question, 'What do you think of this client?')

        response = responses[0]
        self.assertEqual(response.token, 'test_response_token')
        self.assertDictEqual(
            response.metadata,
            dict(
                browser='touch',
                date_land='2017-02-20 22:22:43',
                date_submit='2017-02-20 22:50:33',
                network_id='abcdef',
                platform='mobile',
                referer='https://underdog.typeform.com/to/test_form_id',
                user_agent='User-Agent'
            )
        )
        self.assertEqual(len(response.answers), 2)

        answers = response.answers
        self.assertEqual(answers[0].answer, 'test-user@underdog.io')
        self.assertEqual(answers[0].question, 'What is your email address?')
        self.assertEqual(answers[0].question_id, 'email_id')
        self.assertEqual(answers[1].answer, 'It is awesome!')
        self.assertEqual(answers[1].question, 'What do you think of this client?')
        self.assertEqual(answers[1].question_id, 'list_id_choice')

    def test_form_get_responses_500(self):
        """
        When requesting the responses for a form
            when the API responds with a 500 error
                 we raise an UnknownException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=500)

            with self.assertRaises(UnknownException):
                form.get_responses()

    def test_form_get_responses_404(self):
        """
        When requesting the responses for a form
            when the API responds with a 404 error
                 we raise a NotFoundException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=404, json=fixtures.FORM_RESPONSE_404)

            with self.assertRaises(NotFoundException):
                form.get_responses()

    def test_form_get_responses_400(self):
        """
        When requesting the responses for a form
            when the API responds with a 400 error
                 we raise a InvalidRequestException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=400, json=fixtures.FORM_RESPONSE_400)

            with self.assertRaises(InvalidRequestException):
                form.get_responses()

    def test_form_get_responses_403(self):
        """
        When requesting the responses for a form
            when the API responds with a 403 error
                 we raise a NotAuthorizedException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=403, json=fixtures.FORM_RESPONSE_403)

            with self.assertRaises(NotAuthorizedException):
                form.get_responses()

    def test_form_get_responses_429(self):
        """
        When requesting the responses for a form
            when the API responds with a 429 error
                 we raise a RateLimitException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=429, json=fixtures.FORM_RESPONSE_429)

            with self.assertRaises(RateLimitException):
                form.get_responses()

    def test_form_get_responses_unknown_code(self):
        """
        When requesting the responses for a form
            when the API responds with an unhandled response code
                 we raise a UnknownException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            # DEV: We need to provide a valid json response otherwise we'll fail at parsing
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=302, json=dict())

            with self.assertRaises(UnknownException):
                form.get_responses()

    def test_form_get_responses_non_json(self):
        """
        When requesting the responses for a form
            when the API responds with a non-json response
                 we raise a UnknownException
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=200, text='I am not json')

            with self.assertRaises(UnknownException):
                form.get_responses()

    def test_form_get_responses_filters(self):
        """
        When requesting the responses for a form
            when requesting with filters
                the request does not fail
                we make the appropriate request
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=200, json=fixtures.FORM_RESPONSE_200)
            response = form.get_responses(
                token='test_response_token',
                completed=True,
                limit=5, offset=5,
                since=1234, until=56789,
            )
            self.assertIsNotNone(response)

            # Assert we made the correct request
            self.assertEqual(m.call_count, 1)
            last_request = m.last_request
            self.assertDictEqual(last_request.qs, dict(
                completed=['true'],
                key=['test_api_key'],
                limit=['5'],
                offset=['5'],
                since=['1234'],
                token=['test_response_token'],
                until=['56789'],
            ))

    def test_form_get_responses_sorting(self):
        """
        When requesting the responses for a form
            when requesting with order by sorting
                the request does not fail
                we make the appropriate request
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=200, json=fixtures.FORM_RESPONSE_200)
            response = form.get_responses(order_by='date_land,desc')
            self.assertIsNotNone(response)

            # Assert we made the correct request
            self.assertEqual(m.call_count, 1)
            last_request = m.last_request
            self.assertDictEqual(last_request.qs, {
                'key': ['test_api_key'],
                'order_by[]': ['date_land,desc'],
            })

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=200, json=fixtures.FORM_RESPONSE_200)
            response = form.get_responses(order_by='date_land')
            self.assertIsNotNone(response)

            # Assert we made the correct request
            self.assertEqual(m.call_count, 1)
            last_request = m.last_request
            self.assertDictEqual(last_request.qs, {
                'key': ['test_api_key'],
                'order_by': ['date_land'],
            })

    def test_form_get_response(self):
        """
        When requesting a single response for a form
            the request does not fail
            we make the appropriate request
        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id', status_code=200, json=fixtures.FORM_RESPONSE_200)
            response = form.get_response(token='test_response_token')
            self.assertIsNotNone(response)

            # Assert we made the correct request
            self.assertEqual(m.call_count, 1)
            last_request = m.last_request
            self.assertDictEqual(last_request.qs, {
                'key': ['test_api_key'],
                'token': ['test_response_token'],
            })

    def test_form_get_response_not_found(self):
        """
        When requesting a single response for a form
            when the requested response is not in the response
                we raise a NotFoundException

        """
        form = Form(api_key='test_api_key', form_id='test_form_id')

        with requests_mock.mock() as m:
            m.get('https://api.typeform.com/v1/form/test_form_id',
                  status_code=200, json=fixtures.FORM_RESPONSE_200_EMPTY)

            with self.assertRaises(NotFoundException):
                form.get_response(token='test_response_token')
