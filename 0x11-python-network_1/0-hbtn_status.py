import urllib.request

# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Send the request and fetch the response
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read().decode('utf-8')

    # Display the response body with tabulation
    print("- Response body -")
    print(body)
