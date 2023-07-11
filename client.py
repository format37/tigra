import requests
import datetime

# Replace with your Flask server's URL
url = 'http://localhost:6000'

# Define some test data
test_data = {
    '$i': 'incomers',
    '$o': 'outgoers',
    '$n': 'attendees',
    '$s': 'counter serial no.',
    '$c': 'card ID',
    '$k': 'card shift start and finish',
    '$d': 'UTC time in sec',
    '$m': 'MD5 hash of summary line with signature added'
}

# Send a POST request to the server
response = requests.post(url, json=test_data)

# Print the server's response
print(response.text)
