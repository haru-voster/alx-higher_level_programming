#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    w = requests.get(url)
    print(w.headers.get('X-Request-Id'))
