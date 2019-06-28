import typing
from .client import Client


class Responses:
    """Typeform Responses API client"""

    def __init__(self, client: Client):
        """Constructor for Typeform Responses class"""
        self.__client = client

    def list(
        self, uid: str, pageSize: int = None, since: str = None, until: str = None,
        after: str = None, before: str = None, includedResponseIds: str = None,
        completed: bool = None, sort: str = None, query: str = None, fields: typing.List[str] = None
    ) -> dict:
        """
        Returns form responses and date and time of form landing and submission.
        """
        return self.__client.request('get', '/forms/%s/responses' % uid, params={
            'page_size': pageSize or None,
            'since': since or None,
            'until': until,
            'after': after,
            'before': before,
            'included_response_ids': includedResponseIds,
            'completed': completed,
            'sort': sort,
            'query': query,
            'fields': fields
        })

    def delete(self, uid: str, includedTokens: typing.Union[str, typing.List[str]]) -> str:
        """
        Delete responses to a form. You must specify the `included_tokens`/`includedTokens` parameter.
        Return a `str` based on success of deletion, `OK` on success, otherwise an error message.
        """
        return self.__client.request('delete', '/forms/%s/responses' % uid, params={
            'included_tokens': includedTokens
        })
