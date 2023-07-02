#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
`http://0.0.0.0:5000/search_user` with the letter as
params
"""
import requests
from sys import argv


if __name__ == '__main__':
    q = len(argv) == 2 and argv[1] or ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    if r.json():
        print(f"[{r.json().get('id')}] {r.json().get('name')}")
    elif len(r.json()) == 0:
        print("No result")
    else:
        print("Not a valid JSON")
