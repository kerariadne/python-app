#!/usr/bin/python

import time
import requests
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
    try:
        ip_address = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        ip_address = "Unable to fetch IP"
    return f"Hello World (Python)! (up {elapsed()})\nInstance IP: {ip_address}\n"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    