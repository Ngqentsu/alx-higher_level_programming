#!/usr/bin/python3
"""Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API
   o display your id.
"""

import requests
from requests.auth import HTTPBasicAuth
import sys
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    basic_auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(res.json().get('id'))
