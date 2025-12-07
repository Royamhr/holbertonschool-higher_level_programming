#!/usr/bin/python3
"""Task 9"""


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]

    try:
        req = requests.get(url, auth=(username, token))
        req.raise_for_status()
        print(req.json()['id'])
    except Exception:
        print(None)
