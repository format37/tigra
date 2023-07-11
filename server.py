from flask import Flask, request
import os
import datetime

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def log_request():
@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def log_request(path):
    print(request.args)
    # use the current timestamp to create a unique filename for each request
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = os.path.join('logs', f'request_{timestamp}.log')

    # save the request data to the file
    with open(filename, 'w') as f:
        f.write(str(request.args))

    return 'Request logged successfully.\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
