#!/usr/bin/python3
"""Python script that takes in a URL and an email,
   sends a POST request to passed URL with email as parameter,
   and displays the body of the response (decoded in utf-8)
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    with requests.post(url, data=data) as response:
        print(response.text)
