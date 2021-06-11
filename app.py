from flask import Flask
import os
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello World"

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run( threaded=True, host='0.0.0.0', port=port)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()