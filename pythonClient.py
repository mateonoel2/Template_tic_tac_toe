import http.client

# Create an HTTP connection
conn = http.client.HTTPConnection("127.0.0.1", 5000)

# Send a GET request
conn.request("GET", "/players")

# Get the response
response = conn.getresponse()

# Print the response status code
print("Status:", response.status)

# Print the response body
print("Response:", response.read().decode())

# Close the connection
conn.close()
