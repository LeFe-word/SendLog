import requests
import os
import configparser
import re
from pathlib import Path

# Конфигурация
#TOKEN =            # Токен бота
#CHAT_ID =          # Ваш chat_id
LOG_FILE = "current_logs.txt"  # Файл с логами
TMP_FILE = "tmp_log.txt"

def clean_logs(log_file_path):
    """
    Удаляет избыточную информацию, такую как ANSI-коды и пустые строки.
    """
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')  # ANSI коды
    cleaned_lines = []
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Удаляем ANSI-коды
                line = ansi_escape.sub('', line)
                # Пропускаем пустые строки
                if line.strip():
                    cleaned_lines.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File {log_file_path} not found.")
        return None
    
    return '\n'.join(cleaned_lines)

def save_cleaned_log(cleaned_data, output_path):
    """
    Сохраняет очищенные логи в новый файл.
    """
    if cleaned_data:
        with open(output_path, 'w') as file:
            file.write(cleaned_data)
        print(f"Cleaned log saved to {output_path}")
    else:
        print("No data to save.")

def send_message(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"  # Для поддержки HTML-форматирования
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Ошибка отправки сообщения: {response.text}")

def send_logs(token, chat_id):
    if not os.path.exists(TMP_FILE):
        print("Файл с логами не найден.")
        return
    
    with open(TMP_FILE, "r") as file:
        logs = file.read()

    # Ограничение Telegram на длину сообщения — 4096 символов
    max_length = 4096
    for i in range(0, len(logs), max_length):
        send_message(logs[i:i + max_length], token, chat_id)

def main():
    # Создаем объект ConfigParser
    config = configparser.ConfigParser()

    # Читаем файл конфигурации
    config.read("send.ini")

    try:
        # Извлекаем данные из секции [Telegram]
        token = config["Telegram"]["token"]
        chat_id = config["Telegram"]["chat_id"]
        #log_file = config["Telegram"]["log_file"]
    except KeyError as e:
        print(f"Error: Missing configuration parameter: {e}")
        return

    cleaned_data = clean_logs(LOG_FILE)
    save_cleaned_log(cleaned_data, TMP_FILE)

    # Отправка логов
    send_logs(token, chat_id)

if __name__ == "__main__":
    main()

