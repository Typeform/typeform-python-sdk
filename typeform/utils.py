from urllib.parse import urlencode


def buildUrlWithParams(url: str, params={}) -> str:
    encoded = urlencode(cleanDict(params))
    return url if (len(encoded) == 0) else (url + '?' + encoded)


def cleanDict(x: dict = {}) -> dict:
    result = {}
    for key in x:
        if x[key] is not None:
            # Check If List
            if isinstance(x[key], (list,)):
                result[key] = ','.join(x[key])
            # Check If Boolean
            elif isinstance(x[key], (bool)):
                if x[key] is True:
                    result[key] = 'true'
                else:
                    result[key] = 'false'
            # Everything Else (Strings/Numbers)
            else:
                result[key] = x[key]
    return result


def mergeDict(x: dict, y: dict) -> dict:
    z = cleanDict(x)
    z.update(cleanDict(y))
    return z
