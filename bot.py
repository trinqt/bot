def main():
    last_update_id = None
    send_message("🤖 Bot Termux đã khởi động!")
    print("Bot đang chạy...")  # In thông báo debug ra màn hình
    while True:
        updates = get_updates(last_update_id)
        if updates.get("ok"):
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                message = update.get("message", {})
                text = message.get("text", "")
                if text:
                    if text.strip().lower() == "ip":
                        ip = get_local_ip()
                        send_message(f"📶 IP local: {ip}")
                        print(f"Đã gửi IP: {ip}")  # In ra terminal
                    else:
                        output = execute_command(text)
                        send_message(f"💻 Output:\n{output}")
                        print(f"Đã gửi output: {output}")  # In ra terminal
        time.sleep(1)
