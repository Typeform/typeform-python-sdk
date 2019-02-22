import typing
from .client import Client


class Forms:
    """Typeform Forms API client"""
    def __init__(self, client: Client):
        """Constructor for Typeform Forms class"""
        self.__client = client
        self.__messages = FormMessages(client)

    @property
    def messages(self):
        return self.__messages

    def create(self, data={}) -> dict:
        """Creates a form"""
        return self.__client.request('post', '/forms', data=data)

    def delete(self, uid: str) -> str:
        """
        Deletes the form with the given form_id and all of the form's responses.
        Return a `str` based on success of deletion, `OK` on success, otherwise an error message.
        """
        return self.__client.request('delete', '/forms/%s' % uid)

    def get(self, uid: str) -> dict:
        """Retrieves a form by the given form_id. Includes any theme and images attached to the form as references."""
        return self.__client.request('get', '/forms/%s' % uid)

    def list(self, page: int = None, pageSize: int = None, search: str = None, workspaceId: str = None) -> dict:
        """
        Retrieves a list of JSON descriptions for all forms in your Typeform account (public and private).
        Forms are listed in reverse-chronological order based on the last date they were modified.
        """
        return self.__client.request('get', '/forms', params={
            'page': page,
            'page_size': pageSize,
            'search': search,
            'workspace_id': workspaceId
        })

    def update(self, uid: str, patch=False, data: any = {}) -> typing.Union[str, dict]:
        """
        Updates an existing form.
        Defaults to `put`.
        `put` will return the modified form as a `dict` object.
        `patch` will return a `str` based on success of change, `OK` on success, otherwise an error message.
        """
        methodType = 'put' if patch is False else 'patch'
        return self.__client.request(methodType, '/forms/%s' % uid, data=data)


class FormMessages:
    def __init__(self, client: Client):
        """Constructor for TypeForm FormMessages class"""
        self.__client = client

    def get(self, uid: str) -> dict:
        """
        Retrieves the customizable messages for a form (specified by form_id) using the form's specified language.
        You can format messages with bold (*bold*) and italic (_italic_) text. HTML tags are forbidden.
        """
        return self.__client.request('get', '/forms/%s/messages' % uid)

    def update(self, uid: str, data={}) -> str:
        """
        Specifies new values for the customizable messages in a form (specified by form_id).
        You can format messages with bold (*bold*) and italic (_italic_) text. HTML tags are forbidden.
        Return a `str` based on success of change, `OK` on success, otherwise an error message.
        """
        return self.__client.request('put', '/forms/%s/messages' % uid, data=data)
