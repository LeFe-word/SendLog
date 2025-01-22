#!/bin/bash

sudo apt install -y python3 python3-pip
python3 --version
sleep 2
pip3 install requests

apt install cron
sudo systemctl start cron
sudo systemctl enable cron

wget https://raw.githubusercontent.com/LeFe-word/SendLog/main/send_logs.py
wget https://raw.githubusercontent.com/LeFe-word/SendLog/main/send_log.sh

echo "Please enter bot token:"
read TOKEN
echo "Chat_id:"
read CHAT_ID

echo "[Telegram]" > send.ini
echo "token = $TOKEN" >> send.ini
echo "chat_id = $CHAT_ID" >> send.ini

#echo "python3 send_logs.py --TOKEN $TOKEN --CHAT_ID $CHAT_ID" >> send_log.sh
chmod +x send_log.sh

echo -e "0 7 * * * ./send_log.sh" > shedule.txt
echo -e "0 19 * * * ./send_log.sh" >> shedule.txt

crontab shedule.txt
#./send_log.sh

