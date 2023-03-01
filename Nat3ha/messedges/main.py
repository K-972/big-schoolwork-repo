from twilio.rest import Client

# twilio password = J$TxF4Wv)hx8!4*J$TxF4Wv)hx8!4*

# Your Twilio account SID and auth token
account_sid = "ACcf8031fc4e123cf5714c68c018fb7056"
auth_token = "c8edf96d4d76a2c1230c98a3d3950d5a"

# Create a Twilio client
client = Client(account_sid, auth_token)

# The message you want to send
message = client.messages.create(
    to="+447397855031",
    from_="+19109094456",
    body="123wensday"
)

# Print the message SID
print(message.sid)
