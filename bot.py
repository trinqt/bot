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
        # Lấy các bản cập nhật (updates) từ Telegram
        res = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 10})
        
        # Kiểm tra dữ liệu nhận được
        data = res.json()
        print(f"📊 Dữ liệu nhận được: {data}")

        if data.get("ok") and data.get("result"):
            for update in data["result"]:
                offset = update["update_id"] + 1  # Cập nhật offset để lấy các bản cập nhật tiếp theo
                message = update.get("message", {})
                text = message.get("text", "").strip()  # Lấy tin nhắn
                print(f"📩 Nhận tin nhắn: {text}")
                
                if text:  # Nếu có tin nhắn
                    send_message(f"Bot đã nhận tin nhắn: {text}")
                else:
                    send_message("❓ Không có tin nhắn nào!")

        time.sleep(1)

    except Exception as e:
        print(f"❌ Lỗi: {e}")
        time.sleep(5)
