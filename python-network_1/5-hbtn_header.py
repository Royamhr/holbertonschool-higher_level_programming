#!/usr/bin/python3
"""TASK 5"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(f'{req.headers["X-Request-Id"]}')
