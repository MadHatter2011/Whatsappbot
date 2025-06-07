import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key from environment variable
@app.route("/")
def index():
    return "Jarvis API online! Use POST /send_message with JSON and Authorization header."

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    to = data.get("to")
    msg = data.get("msg")

    if not to or not msg:
        return jsonify({"error": "Missing 'to' or 'msg' fields"}), 400

    # Simulate sending message
    print(f"Sending message to {to}: {msg}")

    return jsonify({
        "status": "message received",
        "to": to,
        "msg": msg
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
