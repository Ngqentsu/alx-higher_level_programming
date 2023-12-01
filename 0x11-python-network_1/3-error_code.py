#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            response_content = response.read()
            print(responseinfo().get('X-Request-Id'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
