#!/usr/bin/python3

"""
This sends a POST request to provided URL with an encoded email address as data and prints the response.

Example Usage:
    python script.py http://example.com/api endpoint@example.com

Inputs:
    url (str): The URL to send the POST request to.
    value (dict): A dictionary containing the email address intended to be encoded.
    data (bytes): A byte string representing the encoded data.

Outputs:
    The response from the POST request, decoded as UTF-8, is printed.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
