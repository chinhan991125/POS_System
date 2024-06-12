import sys
sys.path.append("c:\\users\\chinhanl\\appdata\\local\\programs\\python\\python38\\lib\\site-packages")
import requests

# The URL where your Flask API is running
url = 'http://localhost:5000/get_data'

# Make the GET request and capture the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Success! Response from API:", response.json())
else:
    print("Failed to get a response from the API. Status code:", response.status_code, "Response:", response.text)