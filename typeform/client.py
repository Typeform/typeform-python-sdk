import requests
import json

from .constants import API_BASE_URL
from .utils import buildUrlWithParams, mergeDict


class Client(object):
    """TypeForm API HTTP client"""

    def __init__(self, token, headers: dict = {}):
        """Constructor for TypeForm API client"""
        self.__headers = mergeDict({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'bearer %s' % token
        }, headers)

    def request(self, method: str, url: str, data: any = {}, params: dict = {}, headers={}) -> requests.Response:
        requestUrl = buildUrlWithParams((API_BASE_URL + url), params)
        requestHeaders = mergeDict(self.__headers, headers)
        requestData = ''

        if type(data) is dict:
            requestData = json.dumps(data) if len(data.keys()) > 0 else ''

        if type(data) is list:
            requestData = json.dumps(data) if len(data) > 0 else ''

        return requests.request(method, requestUrl, data=requestData, headers=requestHeaders)
