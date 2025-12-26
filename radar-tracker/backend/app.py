from flask import Flask, jsonify, send_from_directory
from tracker import update
import os

app = Flask(__name__)

# Route to serve JSON data
@app.route("/data")
def data():
    return jsonify(update())

# Route to serve frontend
@app.route("/")
def index():
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')
    return send_from_directory(frontend_dir, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
