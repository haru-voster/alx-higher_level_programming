#!/usr/bin/python3
# haru-voster
""" fetches https://alx-intranet.hbtn.io/status
"""
from sys import argv
import urllib.request as req

if __name__ == "__main__":
    url = argv[1]

    with req.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
