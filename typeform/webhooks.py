import typing
from .client import Client


class Webhooks:
    """Typeform Webhooks API client"""

    def __init__(self, client: Client):
        """Constructor for Typeform Webhooks class"""
        self.__client = client

    def list(self, uid: str) -> dict:
        """
        Returns form webhooks and date and time of form landing and submission.
        """
        return self.__client.request('get', '/forms/%s/webhooks' % uid)


    def get(self, uid: str, tag: str) -> dict:
        """
        Returns form webhooks and date and time of form landing and submission.
        """
        return self.__client.request('get', '/forms/%s/webhooks/%s' % (uid,tag))

    def create_update(self, uid: str, tag: str, data={}) -> dict:
        """
        Create or update a webhook.
        {
            'url': url,  str
            'enabled': enabled,  bool
            'secret': secret,  str
            'verify_ssl': verify_ssl  bool
        }
        """
        return self.__client.request(
            'put', '/forms/%s/webhooks/%s' % (uid,tag), data=data
        )

    def delete(self, uid: str, tag: str) -> str:
        """
        Delete webhooks to a form.
        Return a `str` based on success of deletion, `OK` on success, otherwise an error message.
        """
        return self.__client.request('delete', '/forms/%s/webhooks/%s' % (uid,tag))
