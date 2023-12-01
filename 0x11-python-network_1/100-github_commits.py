#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge
   - The first argument will be the repository name
   - The second argument will be the owner name
"""

import requests
from sys import argv


if __name__ == "__main__":
    rep_name = argv[1]
    rep_owner = argv[2]
    url = f'https://api.github.com/repos/{rep_owner}/{rep_name}/commits'

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            auth_name = commit.get("commit", {}).get("author", {}).get("name")
            print("{}: {}".format(sha, auth_name))

    except requests.RequestException as e:
        print("Error: {}".format(e))
    except IndexError:
        pass
