#!/usr/bin/python3
""" takes a URL, sends a request to the URL and displays the value of
the `X-Request-Id` variable found in the header of the
response
"""

from urllib.request import Request, urlopen
from sys import argv


url_request = Request(argv[1])

with urlopen(url_request) as r:
    print(r.info()['X-Request-Id'])
