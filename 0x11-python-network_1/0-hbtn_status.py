#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import Request, urlopen

url_request = Request("https://alx-intranet.hbtn.io/status")

with urlopen(url_request) as r:
    con_str = r.read()
    print(
        f"Body response:\n\t- type: {type(con_str)}\n\t- content: {con_str}\
        \n\t- utf8 content: {str(object=con_str, encoding='utf-8')}\n")
