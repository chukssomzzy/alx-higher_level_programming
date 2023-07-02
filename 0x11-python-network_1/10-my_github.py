#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and uses the
Github api to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    header = {"Authorization":
              "Bearer " + argv[2],
              "X-Github-Api-Version": "2022-11-28",
              "Accept": "application/vnd.github+json"}

    r = requests.get(f"https://api.github.com/users/{argv[1]}", headers=header)
    print(r.json().get('id'))
