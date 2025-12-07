#!/usr/bin/python3
"""Task 7"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = requests.get(url)
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as error:
        print(f"Error code: {error.response.status_code}")
