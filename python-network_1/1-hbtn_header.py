#!/usr/bin/python3
"""Task 1"""


import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get("X-Request-Id")
        print(x_request_id)
