import requests
import datetime
import sys
import os

def main():
    # Check if the IP address was passed as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python client.py <server-ip>")
        sys.exit(1)

    # Get the server's IP address from the command-line argument
    server_ip = sys.argv[1]
    url = f'http://{server_ip}:6000'

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


if __name__ == '__main__':
    main()
