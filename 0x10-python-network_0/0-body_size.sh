#!/bin/bash

# Check if the URL argument is provided
if [ $# -eq 0 ]; then
    echo "Please provide a URL."
    exit 1
fi

# Get the URL from the command-line argument
url=$1

# Send the request and store the response in a temporary file
response=$(mktemp)
curl -s -o "$response" "$url"

# Get the size of the response body in bytes
size=$(wc -c < "$response")

# Display the size of the response body
echo "Size of the response body: $size bytes"

# Cleanup the temporary file
rm "$response"
