#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" -w "%{http_code}" "$1"

# Check if curl was successful
if [ $? -ne 0 ]; then
    echo "Failed to retrieve the URL."
    rm -f "$response_file"
    exit 1
fi

# Extract the HTTP status code from the response
http_status=$(tail -n1 "$response_file")
if [ "$http_status" -eq 200 ]; then
    # Display the body of the response
    head -n-1 "$response_file"
else
    echo "HTTP Status Code: $http_status"
fi

# Clean up the temporary response file
rm -f "$response_file"
