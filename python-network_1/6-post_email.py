#!/usr/bin/python3
"""Task 6"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    values = {"email": mail}
    req = requests.post(url, values)
    print(req.text)
