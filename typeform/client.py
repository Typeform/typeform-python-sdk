import requests

from .compat import urlparse
from .errors import (NotAuthorizedException, NotFoundException, InvalidRequestException,
                     RateLimitException, UnknownException)


class Client(object):
    """TypeForm API client"""
    BASE_URL = 'https://api.typeform.com/v1/'

    def __init__(self, api_key):
        """Constructor for TypeForm API client"""
        super(Client, self).__init__()

        self.api_key = api_key
        self._client = requests.Session()
        self._client.headers = {
            'User-Agent': 'python-typeform/0.1.0',
        }

    def _request(self, method, path, params=None):
        """Helper method to make requests to the TypeForm API"""
        # Append our API key on to the request params
        if params is None:
            params = dict()
        params['key'] = self.api_key

        # Get our full request URI, e.g. `form/abc123` -> `https://api.typeform.com/v1/form/abc123`
        url = urlparse.urljoin(self.BASE_URL, path)

        # Make our API request
        resp = self._client.request(method=method, url=url, params=params)

        # On 500 error we don't get JSON, so no reason to even try
        if resp.status_code == 500:
            raise UnknownException('typeform client received 500 response from api')

        # Attempt to decode our JSON
        # DEV: In every case (other than 500) we have gotten JSON back, but catch exception just in case
        try:
            data = resp.json()
        except ValueError:
            raise UnknownException('typeform client could not decode json from response')

        # Good response, just return it
        if resp.status_code == 200:
            return data

        # Handle any exceptions
        message = data.get('message')
        if resp.status_code == 404:
            raise NotFoundException(message)
        elif resp.status_code == 403:
            raise NotAuthorizedException(message)
        elif resp.status_code == 400:
            raise InvalidRequestException(message)
        elif resp.status_code == 429:
            raise RateLimitException(message)

        # Hmm, not sure how we got here, just raise hell
        raise UnknownException(
            'typeform client received unknown response status code {code!r}'.format(code=resp.status_code)
        )
