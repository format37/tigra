from flask import Flask, request
import os
import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def log_request():
    print('request.data')
    # use the current timestamp to create a unique filename for each request
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = os.path.join('logs', f'request_{timestamp}.log')

    # save the request data to the file
    with open(filename, 'w') as f:
        f.write(str(request.data))

    return 'Request logged successfully.\n'


if __name__ == '__main__':
    app.run(port=5000)
