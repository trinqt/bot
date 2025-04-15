import requests
import time

BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"
CHAT_ID = "5197540151"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

offset = None

def send_message(text):
    print(f"📤 Gửi tin nhắn: {text}")
    requests.post(f"{URL}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

# Gửi thông báo bot đang chạy
send_message("🤖 Bot đang chạy...")

while True:
    try:
        res = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 10})
        data = res.json()

        if data.get("ok") and data.get("result"):
            for update in data["result"]:
                offset = update["update_id"] + 1
                message = update.get("message", {})
                text = message.get("text", "").strip()
                print(f"📩 Nhận tin nhắn: {text}")
                send_message(f"Bot đã nhận tin nhắn: {text}")

        time.sleep(1)

    except Exception as e:
        print(f"❌ Lỗi: {e}")
        time.sleep(5)
