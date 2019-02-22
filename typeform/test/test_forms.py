from unittest import TestCase
import requests_mock
import urllib.parse

from .fixtures import TOKEN

from typeform import Typeform
from typeform.constants import API_BASE_URL


class FormsTestCase(TestCase):
    def setUp(self):
        self.forms = Typeform(TOKEN).forms
        form = self.forms.create({
            'title': 'title'
        })
        self.formID = form.get('id')

    def tearDown(self):
        list = self.forms.list()
        forms = list.get('items', [])
        for form in forms:
            self.forms.delete(form.get('id'))

    def test_forms_returns_method_and_path(self):
        """
        get all forms has the correct method and path
        """
        with requests_mock.mock() as m:
            m.get(API_BASE_URL+'/forms', json={})
            self.forms.list()

            history = m.request_history
            self.assertEqual(history[0].url, API_BASE_URL+'/forms')
            self.assertEqual(history[0].method, 'GET')

    def test_forms_correct_params(self):
        """
        paramters are sent correctly
        """
        with requests_mock.mock() as m:
            m.get(API_BASE_URL+'/forms', json={})
            self.forms.list(page=2, pageSize=10, search='hola', workspaceId='abc')

            history = m.request_history
            query = history[0].url.split('?')[1]
            params = dict(urllib.parse.parse_qs(query))

            self.assertEqual(params.pop('page')[0], '2')
            self.assertEqual(params.pop('page_size')[0], '10')
            self.assertEqual(params.pop('search')[0], 'hola')
            self.assertEqual(params.pop('workspace_id')[0], 'abc')

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
        with requests_mock.mock() as m:
            m.get(API_BASE_URL+'/forms/'+self.formID, json={})
            self.forms.get(self.formID)

            history = m.request_history
            self.assertEqual(history[0].method, 'GET')

    def test_forms_update_updates_a_form(self):
        """
        update updates a form
        """
        title = 'hola'
        result = self.forms.update(self.formID, data={
            'title': title
        })

        self.assertEqual(result.get('title'), title)

    def test_forms_update_as_patch_updates_a_form(self):
        """
        update as patch updates a form
        """
        result = self.forms.update(self.formID, patch=True, data=[{
            'op': 'replace',
            'path': '/title',
            'value': 'aloha'
        }])

        self.assertEqual(result, 'OK')

    def test_forms_update_sets_put_method_in_request_by_default(self):
        """
        update sets put method in request by default
        """
        with requests_mock.mock() as m:
            m.put(API_BASE_URL+'/forms/'+self.formID, json={})
            self.forms.update(self.formID, data={
                'title': 'title'
            })

            history = m.request_history

            self.assertEqual(history[0].method, 'PUT')

    def test_forms_delete_removes_the_correct_uid_form(self):
        """
        delete removes the correct uid form
        """
        get1Result = self.forms.get(self.formID)
        self.assertEqual(get1Result.get('id'), self.formID)
        self.forms.delete(self.formID)
        try:
            self.forms.get(self.formID)
        except Exception as err:
            error = str(err)
        self.assertEqual(error, 'Non existing form with uid %s' % self.formID)

    def test_forms_create_has_the_correct_path_and_method(self):
        """
        create has the correct path and method
        """
        with requests_mock.mock() as m:
            m.post(API_BASE_URL+'/forms', json={})
            self.forms.create({
                'title': 'hola'
            })

            history = m.request_history

            self.assertEqual(history[0].method, 'POST')
            self.assertEqual(history[0].url, API_BASE_URL+'/forms')

    def test_forms_create_creates_a_new_form(self):
        """
        create creates a new form
        """
        createResult = self.forms.create({
            'title': 'hola'
        })

        formID = createResult.get('id')

        getResult = self.forms.get(formID)

        self.assertIsNone(createResult.get('code', None))
        self.assertEqual(getResult.get('id'), formID)

    def test_forms_get_messages_has_the_correct_path_and_method(self):
        """
        get messages has the correct path and method
        """
        with requests_mock.mock() as m:
            m.get(API_BASE_URL+'/forms/'+self.formID+'/messages', json={})
            self.forms.messages.get(self.formID)

            history = m.request_history

            self.assertEqual(history[0].method, 'GET')
            self.assertEqual(history[0].url, API_BASE_URL+'/forms/'+self.formID+'/messages')

    def test_forms_update_messages_has_the_correct_path_and_method(self):
        """
        update messages has the correct path and method
        """
        with requests_mock.mock() as m:
            m.put(API_BASE_URL+'/forms/'+self.formID+'/messages')
            self.forms.messages.update(self.formID)

            history = m.request_history

            self.assertEqual(history[0].method, 'PUT')
            self.assertEqual(history[0].url, API_BASE_URL+'/forms/'+self.formID+'/messages')
