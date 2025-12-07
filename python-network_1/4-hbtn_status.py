#!/usr/bin/python3
"""Task 4"""


import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    body = req.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
