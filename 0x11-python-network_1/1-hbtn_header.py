#!/usr/bin/python3
""" takes a URL, sends a request to the URL and displays the value of
the `X-Request-Id` variable found in the header of the
response
"""

import urllib.request
import sys

if __name__ == "__main__":
    url_request = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(url_request) as r:
        print(r.info().get('X-Request-Id'))
