import os
import requests
import time

BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"  # Thay bằng token của bạn
CHAT_ID = "5197540151"  # Thay bằng chat ID của bạn
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Hàm gửi tin nhắn tới Telegram
def send_message(text):
    response = requests.post(API_URL, data={"chat_id": CHAT_ID, "text": text})
    if response.status_code != 200:
        print(f"Error sending message: {response.status_code}")
    else:
        print("Message sent successfully!")

# Lấy địa chỉ IP local của thiết bị
def get_local_ip():
    try:
        ip = os.popen('ip addr show wlan0').read().split('inet ')[1].split('/')[0]
        return ip
    except IndexError:
        return "Không thể lấy IP!"

# Thực thi lệnh hệ thống
def execute_command(command):
    try:
        result = os.popen(command).read()
        return result if result else "Không có kết quả!"
    except Exception as e:
        return f"Lỗi khi thực thi lệnh: {e}"

# Hàm chính để kiểm tra và gửi tin nhắn
def main():
    last_update_id = None
    send_message("🤖 Bot Termux đã khởi động!")  # Gửi thông báo khi bot khởi động
    print("Bot đang chạy...")  # In ra màn hình để biết bot đang chạy

    while True:
        # Lấy cập nhật tin nhắn từ bot
        updates = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id}").json()
        
        if updates.get("ok"):
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1  # Cập nhật ID tin nhắn mới nhất
                message = update.get("message", {})
                text = message.get("text", "")
                
                if text:
                    print(f"Nhận lệnh: {text}")  # In ra lệnh đã nhận từ Telegram

                    if text.strip().lower() == "ip":
                        # Gửi địa chỉ IP local
                        ip = get_local_ip()
                        send_message(f"📶 IP local của bạn là: {ip}")
                    else:
                        # Thực thi lệnh hệ thống
                        output = execute_command(text)
                        send_message(f"💻 Output:\n{output}")
        
        time.sleep(1)  # Dừng 1 giây trước khi kiểm tra lại

if __name__ == "__main__":
    main()
