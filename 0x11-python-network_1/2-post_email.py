#!/usr/bin/python3
"""Python script that takes in a URL and an email,
   sends a POST request to passed URL with email as parameter,
   and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({'email': email}).encode("ascii")
    with urllib.request.urlopen(url, data=data) as response:
        print (response.read().decode('utf-8'))
