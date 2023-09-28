#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send an HTTP OPTIONS request to the URL and display the allowed methods
allowed_methods=$(curl -s -i -X OPTIONS "$1" | grep "Allow:" | sed 's/Allow: //')

# Check if curl was successful
if [ $? -ne 0 ]; then
    echo "Failed to retrieve the allowed methods for the URL."
    exit 1
fi

# Display the allowed methods
echo "$allowed_methods"
