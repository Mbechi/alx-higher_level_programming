#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send the request using curl and capture the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$status_code"
