import typing
from .client import Client


class Themes:
    """Typeform Forms API client"""
    def __init__(self, client: Client):
        """Constructor for Typeform Theme class"""
        self.__client = client

    @property
    def messages(self):
        return self.__messages

    def get(self, uid: str) -> dict:
        """Retrieves a form by the given form_id. Includes any theme and images attached to the form as references."""
        return self.__client.request('get', '/themes/%s' % uid)

    def list(self, page: int = None, pageSize: int = None) -> dict:
        """
        Retrieves a list of JSON descriptions for all themes in your Typeform account (public and private). Themes are listed in reverse-chronological order based on the date you added them to your account.
        """
        return self.__client.request('get', '/themes', params={
            'page': page,
            'page_size': pageSize,
        })

    