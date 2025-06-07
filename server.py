# server.py
from flask import Flask, request, jsonify
app = Flask(__name__)
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
secret = os.getenv("ESP32_SECRET")

# Message inbox (holds latest incoming msg)
latest_msg = {"from": "", "msg": ""}

# Message outbox (response from ESP32)
response_msg = {"to": "", "msg": ""}

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

@app.route("/respond", methods=["POST"])
def set_response():
    data = request.json
    token = request.headers.get("Authorization")

    if token != os.getenv("ESP32_SECRET"):
        return jsonify({"error": "Unauthorized"}), 401

    response_msg["to"] = data.get("to")
    response_msg["msg"] = data.get("msg")
    return jsonify({"status": "response saved"})    
    return jsonify(response_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
