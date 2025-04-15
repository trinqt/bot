import requests

BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"
CHAT_ID = "5197540151"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

message = "Hello, this is a test message from the bot!"

response = requests.post(API_URL, data={"chat_id": CHAT_ID, "text": message})

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message!")
