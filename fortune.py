#!/usr/bin/python3

import subprocess

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fortune')
def fortune():
    return jsonify({'fortune': subprocess.check_output(['fortune']).decode('utf-8')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337);
