#!/usr/bin/python3
"""list 10 commits"""


from sys import argv
import requests


if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json",
               "X-Github-Api-Version": '2022-11-28'}

    params = {'per_page': 10}
    r = requests.get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}/\
commits", params=params, headers=headers)
    for commit in r.json():
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
