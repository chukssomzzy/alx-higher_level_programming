#!/usr/bin/python3

"""takes in a URL, sends a request to the URL and displays the
body of the response
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        req_url = Request(argv[1])
        with urlopen(req_url) as r:
            print(str(object=r.read(), encoding="utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
