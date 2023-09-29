#!/usr/bin/python3

"""
This Python code snippet script sends a POST request to a provided URL with a payload containing a letter then receives a response in JSON format. Thereafter, it prints the ID and name from the response if it is not empty.

Example Usage:
    python script.py A
This command will send a POST request to "http://0.0.0.0:5000/search_user" with a payload containing the letter "A". If the response is not empty, it will print the ID and name from the response.

Inputs:
    - sys.argv: A list of command-line arguments passed to the script.
    - sys.argv[1]: The second command-line argument, which is the letter to be included in the payload.

Flow:
1. The script checks if there is a command-line argument specified. If not, it sets the `letter` variable to an empty string.
2. The script creates a payload dictionary with the letter as the value for the key "q".
3. The script sends a POST request to the specified URL with the payload.
4. It tries to parse the response as JSON.
5. If the response is an empty dictionary, it prints "No result".
6. Otherwise, it prints the ID and name from the response.

Outputs:
    - If the response is an empty dictionary, it prints "No result".
    - If the response is not empty, it prints the ID and name from the response.
"""

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
