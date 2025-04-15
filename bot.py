import requests
import time
import socket

BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"
CHAT_ID = "5197540151"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

offset = None

def send_message(text):
    print(f"📤 Gửi tin nhắn về Telegram: {text}")
    requests.post(f"{URL}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Không lấy được IP"

print("🤖 Bot đang chạy...")

while True:
    try:
        res = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 10})
        data = res.json()

        if data.get("ok") and data.get("result"):
            for update in data["result"]:
                offset = update["update_id"] + 1
                message = update.get("message", {})
                text = message.get("text", "").strip().lower()
                print(f"📩 Nhận tin nhắn: {text}")

                if text == "ip":
                    ip = get_local_ip()
                    send_message(f"📶 IP local của bạn là: {ip}")

                elif text == "hi" or text == "hello":
                    send_message("👋 Xin chào! Gửi 'ip' để lấy IP local.")

                else:
                    send_message("❓ Không hiểu lệnh. Gửi 'ip' để lấy IP.")

        time.sleep(1)

    except Exception as e:
        print(f"❌ Lỗi: {e}")
        time.sleep(5)
