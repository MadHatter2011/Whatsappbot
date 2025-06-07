import os
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Grab your Twilio credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = "whatsapp:+14155238886"  # Twilio sandbox WhatsApp number

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/")
def index():
    return "Jarvis API online! Use POST /send_message with JSON."

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    to = data.get("to")
    msg = data.get("msg")

    if not to or not msg:
        return jsonify({"error": "Missing 'to' or 'msg' fields"}), 400

    try:
        message = client.messages.create(
            body=msg,
            from_=TWILIO_WHATSAPP_FROM,
            to=to
        )
        print(f"Sent message SID: {message.sid} to {to}")

        return jsonify({
            "status": "message sent",
            "to": to,
            "msg": msg,
            "sid": message.sid
        })
    except Exception as e:
        print(f"Error sending message: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
