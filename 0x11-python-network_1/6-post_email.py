#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import requests

# Get the URL and email from the command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Send the POST request with the email as a parameter
response = requests.post(url, data={'email': email})

# Display the response body
print(response.text)
