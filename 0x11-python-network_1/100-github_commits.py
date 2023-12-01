#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge
   - The first argument will be the repository name
   - The second argument will be the owner name
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])
    try:
        response = resquests.get(url).json()
        for index, response in enumerate(response[:10]):
            try:
                sha = commit["sha"]
                author_name = commit["commit"]["author"]["name"]
                print("{}: {}".format(sha, author_name))
            except (KeyError, IndexError):
                pass
    except requests.RequestException as e:
        pass
