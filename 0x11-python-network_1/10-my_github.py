#!/usr/bin/python3

"""
This script forms part of a larger script that makes a GET request to the GitHub API to recover the user ID using basic authentication.

Example Usage:
    python script.py username password

Inputs:
    username (str): A string representing the GitHub username.
    password (str): A string representing the GitHub password.

Outputs:
    The user ID of the authenticated GitHub user.

Code Analysis:
1. Import the necessary modules and classes.
2. Check if the script is being run as the main program.
3. Create an instance of `HTTPBasicAuth` using the provided `username` and `password`.
4. Make a GET request to the GitHub API endpoint `https://api.github.com/user` with the authentication.
5. Retrieve the response as JSON and extract the user ID.
6. Print the user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
