#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Use curl to send a GET request and store the response in a temporary file
response_file=$(mktemp)
curl -sI "$1" -o "$response_file"

# Check if curl was successful
if [ $? -ne 0 ]; then
	echo "Failed to retrieve the URL."
	exit 1
fi

# Extract the content length from the response headers and display it
content_length=$(grep -i '^Content-Length:' "$response_file" | awk '{print $2}' | tr -d '\r\n')
echo "$content_length"

# Clean up the temporary response file
rm -f "$response_file"
