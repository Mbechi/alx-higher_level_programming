#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request with the custom header and store the response in a temporary file
response_file=$(mktemp)
curl -s -H "X-School-User-Id: 98" -o "$response_file" "$1"

# Check if curl was successful
if [ $? -ne 0 ]; then
    echo "Failed to retrieve the URL."
    rm -f "$response_file"
    exit 1
fi

# Display the body of the response
cat "$response_file"

# Clean up the temporary response file
rm -f "$response_file"
