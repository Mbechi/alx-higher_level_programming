#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Set the email and subject variables
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with the specified parameters and store the response in a temporary file
response_file=$(mktemp)
curl -s -X POST -d "email=$email&subject=$subject" -o "$response_file" "$1"

# Check if curl was successful
if [ $? -ne 0 ]; then
    echo "Failed to send the POST request."
    rm -f "$response_file"
    exit 1
fi

# Display the body of the response
cat "$response_file"

# Clean up the temporary response file
rm -f "$response_file"
