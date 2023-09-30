#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.request as req
import urllib.parse as parse

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    email = parse.urlencode(values).encode("ascii")

    request = req.Request(url, email)
    with req.urlopen(request) as response:
        page = response.read()
        print(page.decode("utf-8"))
