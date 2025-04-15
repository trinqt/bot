import requests
import time
import subprocess

BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"
CHAT_ID = "5197540151"

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def send_message(text):
    url = f"{API_URL}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def get_local_ip():
    try:
        result = subprocess.check_output("ip addr show wlan0", shell=True).decode()
        for line in result.split("\n"):
            if "inet " in line:
                return line.strip().split(" ")[1].split("/")[0]
        return "Không tìm thấy IP"
    except Exception as e:
        return f"Lỗi lấy IP: {e}"

def execute_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
        return result if result.strip() else "(Không có output)"
    except subprocess.CalledProcessError as e:
        return f"Lỗi:\n{e.output.decode()}"

def main():
    last_update_id = None
    send_message("🤖 Bot Termux đã khởi động!")
    while True:
        updates = get_updates(last_update_id)
        if updates.get("ok"):
            for update in updates["result"]:
                last_update_id = update["update_id"] +_
