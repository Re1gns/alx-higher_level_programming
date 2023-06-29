#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests

# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Send the request and fetch the response
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response body
    body = response.text

    # Display the response body with tabulation
    print("- Response body -")
    print(body)
else:
    print("Request failed with status code:", response.status_code)
