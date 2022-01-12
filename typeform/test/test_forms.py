from unittest import TestCase
import requests_mock
import urllib.parse

from .fixtures import MOCK, TOKEN, WORKSPACE, WORKSPACE_ID

from typeform import Typeform
from typeform.constants import API_BASE_URL


class FormsTestCase(TestCase):
    def setUp(self):
        self.forms = Typeform(TOKEN).forms
        if not MOCK:
            form = self.forms.create(dict(title="Form's test form", workspace={'href': WORKSPACE}))
            self.formID = form.get('id')
        else:
            self.formID = 'MOCK-FORM-ID'

    def tearDown(self):
        if not MOCK:
            list = self.forms.list(workspaceId=WORKSPACE_ID)
            forms = list.get('items', [])
            for form in forms:
                self.forms.delete(form.get('id'))

    def test_forms_returns_method_and_path(self):
        """
        get all forms has the correct method and path
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.get(API_BASE_URL+'/forms', json={})
            self.forms.list(workspaceId=WORKSPACE_ID)

            history = m.request_history
            self.assertEqual(history[0].url, API_BASE_URL+'/forms?workspace_id={}'.format(WORKSPACE_ID))
            self.assertEqual(history[0].method, 'GET')

    def test_forms_correct_params(self):
        """
        paramters are sent correctly
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.get(API_BASE_URL+'/forms', json={})
            self.forms.list(page=2, pageSize=10, search='forms_correct_params', workspaceId=WORKSPACE_ID)

            history = m.request_history
            query = history[0].url.split('?')[1]
            params = dict(urllib.parse.parse_qs(query))

            self.assertEqual(params.pop('page')[0], '2')
            self.assertEqual(params.pop('page_size')[0], '10')
            self.assertEqual(params.pop('search')[0], 'forms_correct_params')
            self.assertEqual(params.pop('workspace_id')[0], WORKSPACE_ID)

    def test_forms_get_correct_id(self):
        """
        get sends the correct UID
        """
        with requests_mock.mock() as m:
            m.get(API_BASE_URL+'/forms/'+self.formID, json={})
            self.forms.get(self.formID)

            history = m.request_history
            self.assertEqual(history[0].url, API_BASE_URL+'/forms/'+self.formID)

    def test_forms_get_sets_get_method(self):
        """
        get sets get method
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.get(API_BASE_URL+'/forms/'+self.formID, json={})
            self.forms.get(self.formID)

            history = m.request_history
            self.assertEqual(history[0].method, 'GET')

    def test_forms_update_updates_a_form(self):
        """
        update updates a form
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            title = 'forms_update_updates_a_form'
            m.put(API_BASE_URL + '/forms/' + self.formID, json=dict(title=title))
            result = self.forms.update(self.formID, data={
                'title': title
            })

            self.assertEqual(result.get('title'), title)

    def test_forms_update_as_patch_updates_a_form(self):
        """
        update as patch updates a form
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.patch(API_BASE_URL+'/forms/'+self.formID, json='OK')
            result = self.forms.update(self.formID, patch=True, data=[
                dict(op='replace', path='/title', value='forms_update_as_patch_updates_a_form')])

            self.assertEqual(result, 'OK')

    def test_forms_update_sets_put_method_in_request_by_default(self):
        """
        update sets put method in request by default
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.put(API_BASE_URL+'/forms/'+self.formID, json={})
            self.forms.update(self.formID, data={
                'title': 'forms_update_sets_put_method_in_request_by_default'
            })

            history = m.request_history

            self.assertEqual(history[0].method, 'PUT')

    def test_forms_delete_removes_the_correct_uid_form(self):
        """
        delete removes the correct uid form
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.get(API_BASE_URL + '/forms/{}'.format(self.formID), json=dict(id=str(self.formID)))
            m.delete(API_BASE_URL + '/forms/{}'.format(self.formID), json={})

            get_one_result = self.forms.get(self.formID)
            self.assertEqual(get_one_result.get('id'), self.formID)
            self.forms.delete(self.formID)
            m.get(API_BASE_URL + '/forms/{}'.format(self.formID),
                  json=dict(code='FORM_NOT_FOUND', description='Non existing form with uid {}'.format(self.formID)))
            try:
                self.forms.get(self.formID)
            except Exception as err:
                error = str(err)
            self.assertEqual(error, 'Non existing form with uid %s' % self.formID)

    def test_forms_create_has_the_correct_path_and_method(self):
        """
        create has the correct path and method
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.post(API_BASE_URL+'/forms', json={})
            self.forms.create(dict(title='forms_create_has_the_correct_path_and_method', workspace={'href': WORKSPACE}))

            history = m.request_history

            self.assertEqual(history[0].method, 'POST')
            self.assertEqual(history[0].url, API_BASE_URL+'/forms')

    def test_forms_create_creates_a_new_form(self):
        """
        create creates a new form
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.post(API_BASE_URL + '/forms', json=dict(id=str(self.formID)))
            m.get(API_BASE_URL + '/forms/{}'.format(self.formID), json=dict(id=str(self.formID)))

            create_result = self.forms.create(dict(
                title='forms_create_creates_a_new_form',
                workspace={'href': WORKSPACE},
            ))

            formID = create_result.get('id')

            result = self.forms.get(formID)

            self.assertIsNone(create_result.get('code', None))
            self.assertEqual(result.get('id'), formID)

    def test_forms_get_messages_has_the_correct_path_and_method(self):
        """
        get messages has the correct path and method
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.get(API_BASE_URL+'/forms/'+self.formID+'/messages', json={})
            self.forms.messages.get(self.formID)

            history = m.request_history

            self.assertEqual(history[0].method, 'GET')
            self.assertEqual(history[0].url, API_BASE_URL+'/forms/'+self.formID+'/messages')

    def test_forms_update_messages_has_the_correct_path_and_method(self):
        """
        update messages has the correct path and method
        """
        with requests_mock.mock(real_http=not MOCK) as m:
            m.put(API_BASE_URL+'/forms/'+self.formID+'/messages')
            self.forms.messages.update(self.formID)

            history = m.request_history

            self.assertEqual(history[0].method, 'PUT')
            self.assertEqual(history[0].url, API_BASE_URL+'/forms/'+self.formID+'/messages')
