#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000 """

import requests
from sys import argv

if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    s = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = s.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
