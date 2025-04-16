#!/bin/bash

# Cập nhật Termux và cài đặt các công cụ cần thiết
pkg update && pkg upgrade -y
pkg install python git curl wget -y

# Cài đặt thư viện Python cần thiết
pip install --upgrade pip
pip install flask requests python-telegram-bot cloudflare

# Cài đặt tmux (nếu bạn muốn chạy lâu dài trong nền)
pkg install tmux -y

# Cài đặt các công cụ khác nếu cần
pkg install openssh -y

# Tạo một thư mục để lưu trữ dự án nếu chưa có
mkdir -p ~/termux-auto
cd ~/termux-auto

# Clone repo từ GitHub nếu chưa có
git clone https://github.com/ten-cua-ban/termux-auto.git
cd termux-auto

# Tạo symlink để chạy khi khởi động
ln -s ~/termux-auto/start.sh ~/.termux/boot/start.sh
chmod +x ~/.termux/boot/start.sh

echo "Cài đặt hoàn tất! Bạn có thể bắt đầu chạy các dịch vụ trong Termux."
