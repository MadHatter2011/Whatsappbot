from twilio.rest import Client

account_sid = "AC8f397004355225efb091f00b64a8f21c"
auth_token = "c9dbd17f0d2fa5044fe2cfefa77086a0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Test message from Boss!',
    to='whatsapp:+919888891945'
)

print("SID:", message.sid)
