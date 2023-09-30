#!/bin/bash
# haru-voster
""" sends a request to the URL and displays the value of the X-Request-Id"""
from sys import argv
import urllib.request as req

if __name__ == "__main__":
    url = argv[1]

    with req.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
