from unittest import TestCase
import requests_mock

from .fixtures import TOKEN

from typeform.client import Client
from typeform.constants import API_BASE_URL


class ClientTestCase(TestCase):
    def test_client_pass_headers(self):
        """
        request pass correct headers
        """
        client = Client(TOKEN)

        with requests_mock.mock() as m:
            m.get(API_BASE_URL+'/forms')
            client.request('GET', '/forms', data={}, params={}, headers={
                'Accepts': 'application/json'
            })

            history = m.request_history
            self.assertEqual(history[0].url, API_BASE_URL+'/forms')
            self.assertEqual(history[0].headers.pop('Content-Type'), 'application/json')
            self.assertEqual(history[0].headers.pop('Accepts'), 'application/json')
            self.assertEqual(history[0].headers.pop('Authorization'), 'bearer %s' % TOKEN)
