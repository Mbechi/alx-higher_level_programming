#!/usr/bin/python3

"""
This code snippet is a standalone script taking a URL as a command-line argument then sending a GET request to URL using the requests library. Thereafter, it checks the status code of the response and prints either the error code or response text.

Example Usage:
    python script.py https://www.example.com

Inputs:
    url (string): The URL to send the GET request at which is passed as a command-line argument.

Outputs:
    If the status code of the response is > or = to 400, the code snippet prints the error code.
    If the status code is < than 400, the code snippet prints the response text.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
