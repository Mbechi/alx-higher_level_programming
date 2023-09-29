#!/usr/bin/python3

"""
Takes  URL as command-line argument and sends request to the URL. Thereafter it prints the value of the "X-Request-Id" header from the response.

Example Usage:
    python script.py https://example.com

Inputs:
    url (string): URL to send request at whichis passed as command-line argument.

Outputs:
    The value of the "X-Request-Id" header from the response is printed.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
