#!/bin/bash

# Check if both URL and JSON file arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON file>"
    exit 1
fi

# Assign the URL and JSON file arguments to variables
url="$1"
json_file="$2"

# Check if the JSON file exists and is readable
if [ ! -f "$json_file" ] || [ ! -r "$json_file" ]; then
    echo "Error: JSON file '$json_file' does not exist or is not readable."
    exit 1
fi

# Send the POST request with the JSON file contents as the request body
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$url")

# Check if the response is valid JSON
if jq '.' <<< "$response" >/dev/null 2>&1; then
    echo "$response"
else
    echo "Not a valid JSON"
fi
