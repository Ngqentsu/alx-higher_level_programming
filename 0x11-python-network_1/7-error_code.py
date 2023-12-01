#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""

import requests
from sys import argv


if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
