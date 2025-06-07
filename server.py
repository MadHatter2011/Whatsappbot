import os
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Load Twilio credentials from environment variables (set these on Render or your server)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = "whatsapp:+14155238886"  # Twilio Sandbox WhatsApp number, keep it like this

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/")
def index():
    return "Jarvis API online! Use POST /send_message with JSON: {to, msg}"

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    to = data.get("to")  # format: whatsapp:+91xxxxxxxxxx
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
            "status": "sent",
            "sid": message.sid,
            "to": to,
            "msg": msg
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
