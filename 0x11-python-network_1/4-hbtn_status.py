#!/usr/bin/python3
# haru-voster
""" fetches https://intranet.hbtn.io/status using requests
"""

import requests

if __name__ == "__main__":
    s = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(s.text)))
    print("\t- content: {}".format(s.text))
