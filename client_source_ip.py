
#client_source_ip.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return '<h1> Source IP address is : ' + ip_addr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
