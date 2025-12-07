#!/usr/bin/python3
"""Task 3"""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            body = body.decode('utf-8')
            print(body)
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
