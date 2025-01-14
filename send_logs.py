import requests
import os
import argparse

# Конфигурация
#TOKEN =            # Токен бота
#CHAT_ID =          # Ваш chat_id
LOG_FILE = "current_logs.txt"  # Файл с логами

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # Для поддержки HTML-форматирования
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Ошибка отправки сообщения: {response.text}")

def send_logs():
    if not os.path.exists(LOG_FILE):
        print("Файл с логами не найден.")
        return
    
    with open(LOG_FILE, "r") as file:
        logs = file.read()

    # Ограничение Telegram на длину сообщения — 4096 символов
    max_length = 4096
    for i in range(0, len(logs), max_length):
        send_message(logs[i:i + max_length])

if __name__ == "__main__":
    send_logs()
