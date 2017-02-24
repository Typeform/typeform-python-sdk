import sys

PY2 = sys.version_info[0] == 2

if PY2:
    import urlparse
else:
    import urllib.parse as urlparse


__all__ = ['urlparse']
