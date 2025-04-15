import requests

BOT_TOKEN = '7661043177:AAEL1xO9C1O4vMnr705gZvPPRMh5JN26VHk'
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Hàm lấy cập nhật tin nhắn từ bot
def get_updates():
    response = requests.get(f"{URL}/getUpdates")
    print(response.json())  # In toàn bộ phản hồi để xem tin nhắn
    return response.json()

get_updates()
