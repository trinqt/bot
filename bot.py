import requests

# Thay đổi BOT_TOKEN và CHAT_ID của bạn tại đây
BOT_TOKEN = "7916172515:AAF1e1Nj8K_F8Xr2LGQyLTKBlYTn9ZlOrIU"
CHAT_ID = "5197540151"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Đảm bảo có một offset hợp lệ, nếu không có offset thì để là 0
offset = 0

# Gửi yêu cầu GET để nhận cập nhật
res = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 10})

# Kiểm tra mã trạng thái HTTP
print(f"HTTP Status Code: {res.status_code}")

# Kiểm tra nếu mã trạng thái là 200 (thành công)
if res.status_code == 200:
    # In ra toàn bộ nội dung phản hồi
    print("Response Text: ")
    print(res.text)

    # Chuyển đổi phản hồi thành JSON để dễ xử lý
    data = res.json()

    # Kiểm tra xem dữ liệu trả về có hợp lệ không
    if data.get("ok"):
        print("Dữ liệu trả về hợp lệ:")
        print(data)  # In ra toàn bộ dữ liệu nhận được
        if data.get("result"):
            print("Tin nhắn mới:")
            for update in data["result"]:
                print(f"Update ID: {update['update_id']}")
                print(f"Message: {update.get('message')}")
        else:
            print("Không có tin nhắn mới.")
    else:
        print("Lỗi trong phản hồi từ Telegram.")
else:
    print(f"Lỗi khi gửi yêu cầu, mã trạng thái: {res.status_code}")
