class TypeFormException(Exception):
    """Base exception that all other exceptions inherit from"""
    pass


class InvalidRequestException(TypeFormException):
    """Exception raised on 400 responses from the API"""
    pass


class NotAuthorizedException(TypeFormException):
    """Exception raised on 403 responses from the API"""
    pass


class RateLimitException(TypeFormException):
    """Exception raised on 429 responses from the API"""
    pass


class UnknownException(TypeFormException):
    """Exception raised when we receive an unknown/unexpected response from the API"""
    pass


class NotFoundException(TypeFormException):
    """Exception raised when we could not the resource requested"""
    pass
