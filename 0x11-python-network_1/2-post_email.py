#!/usr/bin/python3

"""takes in a URL and an email sends a POST request to the passed URL with the
email as a prarameter and displays the body of response
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    value = {"email": argv[2]}
    data = urlencode(value)
    data = data.encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as r:
        print(str(object=r.read(), encoding='utf-8'))
