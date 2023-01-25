from .forms import Forms
from .themes import Themes
from .images import Images
from .responses import Responses
from .client import Client

__all__ = ['Typeform']


class Typeform:
    """Typeform API client"""

    def __init__(self, token: str, headers: dict = {}):
        """Constructor for Typeform API client"""
        client = Client(token, headers=headers)
        self.__forms = Forms(client)
        self.__themes = Themes(client)
        self.__images = Images(client)
        self.__responses = Responses(client)

    @property
    def forms(self) -> Forms:
        return self.__forms

    @property
    def themes(self) -> Themes:
        return self.__themes

    @property
    def images(self) -> Images:
        return self.__images

    @property
    def responses(self) -> Responses:
        return self.__responses
