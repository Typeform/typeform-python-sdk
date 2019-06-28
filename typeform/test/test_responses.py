from unittest import TestCase
import requests_mock
import urllib.parse

from .fixtures import TOKEN

from typeform import Typeform
from typeform.constants import API_BASE_URL


class ResponsesTestCase(TestCase):
    def setUp(self):
        self.forms = Typeform(TOKEN).forms
        self.responses = Typeform(TOKEN).responses
        form = self.forms.create({
            'title': 'title'
        })
        self.formID = form.get('id')

    def tearDown(self):
        list = self.forms.list()
        forms = list.get('items', [])
        for form in forms:
            self.forms.delete(form.get('id'))

    def test_list_returns_method_and_path(self):
        """
        get all responses has the correct method and path
        """
        with requests_mock.mock() as m:
            url = API_BASE_URL+'/forms/'+self.formID+'/responses'
            m.get(url, json={})
            self.responses.list(self.formID)

            history = m.request_history
            self.assertEqual(history[0].url, url)
            self.assertEqual(history[0].method, 'GET')

    def test_list_correct_params(self):
        """
        paramters are sent correctly
        """
        with requests_mock.mock() as m:
            url = API_BASE_URL+'/forms/'+self.formID+'/responses'
            m.get(url, json={})
            self.responses.list(
                self.formID, pageSize='100', since='2000-01-01T00:00:00Z', completed=True, fields=['1', '2']
            )

            history = m.request_history
            query = history[0].url.split('?')[1]
            params = dict(urllib.parse.parse_qs(query))

            self.assertEqual(params.pop('page_size')[0], '100')
            self.assertEqual(params.pop('since')[0], '2000-01-01T00:00:00Z')
            self.assertEqual(params.pop('completed')[0], 'true')
            self.assertEqual(params.pop('fields')[0], '1,2')

    def test_list_fetches_responses(self):
        """
        get all responses does not throw an error
        """
        result = self.responses.list(self.formID)
        self.assertEqual(result.pop('total_items'), 0)

    def test_list_fetches_responses_with_params(self):
        """
        get all responses does not throw an error with paramters
        """
        result = self.responses.list(
            self.formID, pageSize=100, since='2000-01-01T00:00:00Z', completed=True, fields=['1', '2']
        )
        self.assertEqual(result.pop('total_items'), 0)

    def test_delete_one_token_returns_method_and_path(self):
        """
        delete response has the correct method and path when deleting one token
        """
        with requests_mock.mock() as m:
            url = API_BASE_URL+'/forms/'+self.formID+'/responses?included_tokens=1'
            m.delete(url, json={})
            self.responses.delete(self.formID, includedTokens='1')

            history = m.request_history
            self.assertEqual(history[0].url, url)
            self.assertEqual(history[0].method, 'DELETE')

    def test_delete_multiple_token_returns_method_and_path(self):
        """
        delete response has the correct method and path when deleting multiple tokens
        """
        with requests_mock.mock() as m:
            url = API_BASE_URL+'/forms/'+self.formID+'/responses?included_tokens=1%2C2%2C3'
            m.delete(url, json={})
            self.responses.delete(self.formID, includedTokens=['1', '2', '3'])

            history = m.request_history
            self.assertEqual(history[0].url, url)
            self.assertEqual(history[0].method, 'DELETE')
