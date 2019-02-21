from urllib.parse import urlencode


def buildUrlWithParams(url: str, params={}) -> str:
    encoded = urlencode(cleanDict(params))
    return url if (len(encoded) == 0) else (url + '?' + encoded)


def cleanDict(x: dict = {}) -> dict:
    result = {}
    for key in x:
        if x[key] is not None:
            result[key] = x[key]
    return result


def includes(param: any, array: list) -> bool:
    result = False
    for value in array:
        if value == param:
            result = True
    return result


def mergeDict(x: dict, y: dict) -> dict:
    z = cleanDict(x)
    z.update(cleanDict(y))
    return z
