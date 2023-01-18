import typing
from .client import Client


class Images:
    """Typeform Forms API client"""
    def __init__(self, client: Client):
        """Constructor for Typeform Images class"""
        self.__client = client

    @property
    def messages(self):
        return self.__messages

    def get(self, uid: str) -> dict:
        """Retrieves an image by the given form_id."""

        return self.__client.request('get', '/images/%s' % uid)

    def list(self) -> dict:
        """
        Retrieves a list of JSON descriptions for all images in your Typeform account. Images are listed in reverse-chronological order based on the date you added them to your account.
        """
        return self.__client.request('get', '/images')

    def upload(self, file_name : str, image : str = None, url : str = None) -> dict:
        """
        Adds an image in your Typeform account.

        Specify the URL of your image or send your image in base64 format, which encodes the image data as ASCII text. You can use a tool like Base64 Image Encoder to get the base64 code for the image you want to add.
        """
        return self.__client.request('post', '/images', data={
            'file_name': file_name,
            'image': image,
        })