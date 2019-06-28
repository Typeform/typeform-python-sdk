import json
import requests
import typing

from .constants import API_BASE_URL
from .utils import buildUrlWithParams, mergeDict


class Client(object):
    """TypeForm API HTTP client"""

    def __init__(self, token: str, headers: dict = {}):
        """Constructor for TypeForm API client"""
        self.__headers = mergeDict({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'bearer %s' % token
        }, headers)

    def request(self, method: str, url: str, data: any = {}, params: dict = {}, headers={}) -> typing.Union[str, dict]:
        requestUrl = buildUrlWithParams((API_BASE_URL + url), params)
        requestHeaders = mergeDict(self.__headers, headers)
        requestData = ''
        if type(data) is dict:
            requestData = json.dumps(data) if len(data.keys()) > 0 else ''

        if type(data) is list:
            requestData = json.dumps(data) if len(data) > 0 else ''

        result = requests.request(method, requestUrl, data=requestData, headers=requestHeaders)
        return self.__validator(result)

    def __validator(self, result: requests.Response) -> typing.Union[str, dict]:
        try:
            body = json.loads(result.text)
        except Exception:
            body = {}

        if type(body) is dict and body.get('code', None) is not None:
            raise Exception(body.get('description'))
        elif result.status_code >= 400:
            raise Exception(result.reason)
        elif len(result.text) == 0:
            return 'OK'
        else:
            return body
