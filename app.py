from flask import Flask, render_template
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def logs():
    if not os.path.exists("storage/parsed_logs.json"):
        return jsonify([])
    with open("storage/parsed_logs.json") as f:
        return jsonify([json.loads(line) for line in f if line.strip()])

@app.route("/alerts")
def alerts():
    if not os.path.exists("alerts/alerts.log"):
        return jsonify([])
    with open("alerts/alerts.log") as f:
        return jsonify([line.strip() for line in f if line.strip()])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

