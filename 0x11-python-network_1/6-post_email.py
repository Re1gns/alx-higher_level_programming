#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL.")
        sys.exit(1)

    url = sys.argv[1]

    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            print(dict(response.headers).get("X-Request-Id"))

    except HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
