"""Code for a flask API to Create, Read, Update, Delete users"""
import os
from flask import jsonify, request, Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)