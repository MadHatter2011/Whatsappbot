from flask import Flask, request, jsonify
import os

app = Flask(__name__)

latest_msg = {"from": "", "msg": ""}
response_msg = {"to": "", "msg": ""}

@app.route("/")
def index():
    return "Jarvis API is online!"

@app.route("/incoming", methods=["POST"])
def receive_message():
    data = request.json
    latest_msg["from"] = data.get("from")
    latest_msg["msg"] = data.get("msg")
    return jsonify({"status": "received"})

@app.route("/poll", methods=["GET"])
def get_latest():
    return jsonify(latest_msg)

@app.route("/respond", methods=["POST"])
def set_response():
    data = request.json
    response_msg["to"] = data.get("to")
    response_msg["msg"] = data.get("msg")
    return jsonify({"status": "response saved"})

@app.route("/get_response", methods=["GET"])
def send_response():
    return jsonify(response_msg)

# Optional: Run locally for testing
if __name__ == "__main__":
    app.run(debug=True)
