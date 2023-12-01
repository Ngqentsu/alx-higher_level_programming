#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        response_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_content)))
        print("\t- content: {}".format(response_content))
        print("\t- utf8 content: {}".format(response_content.decode("utf-8")))
