#!/usr/bin/python3
# haru-voster
""" fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        dt = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(dt)))
        print("\t- content: {}".format(dt))
        print("\t- utf8 content: {}".format(dt.decode("utf-8")))
