#!/usr/bin/python

import time
import socket
from flask import Flask

app = Flask(__name__)

START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"Hello World (Python)! (up {elapsed()})\nInstance IP: {ip_address}\n"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)