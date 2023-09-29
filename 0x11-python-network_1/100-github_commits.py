#!/usr/bin/python3

"""
Recover and print the SHA as well as author name of the latest 10 commits from a GitHub repository.

Example Usage:
    python3 script.py <repository> <owner>

Inputs:
    repository (str): The name of the GitHub repository.
    owner (str): The username of the repository owner.

Outputs:
    None. The code snippet prints the SHA and author name of the latest 10 commits from the specified GitHub repository.

Code Snippet:
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
