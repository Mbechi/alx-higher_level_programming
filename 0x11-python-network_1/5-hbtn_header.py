#!/usr/bin/python3

"""
This standalone script sends an HTTP GET request to a provided URL then prints the value of the "X-Request-Id" header from the response.

Example Usage:
    python script.py https://example.com

Inputs:
    url (str): The URL to send the GET request at, obtained from the command-line argument `sys.argv[1]`.

Outputs:
    The value of the "X-Request-Id" header from the HTTP response.

Code Analysis:
1. The code snippet imports the `sys` and `requests` modules.
2. It checks if the script is being run as the main module.
3. It retrieves the URL from the command-line argument `sys.argv[1]` and assigns it to the variable `url`.
4. It sends an HTTP GET request to the specified URL using `requests.get(url)`.
5. It retrieves the value of the "X-Request-Id" header from the response using `r.headers.get("X-Request-Id")`.
6. It prints the value of the "X-Request-Id" header.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
