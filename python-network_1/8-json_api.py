#!/usr/bin/python3
"""TASK 8"""


import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    values = {"q": q}

    try:
        req = requests.post(url, values)
        if len(req.json()) == 0:
            print("No result")
        else:
            print(f"[{req.json()['id']}] {req.json()['name']}")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
