#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

from mypackage import testvar

@app.route("/")
def hello():
    return f"Hello World! {testvar}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
