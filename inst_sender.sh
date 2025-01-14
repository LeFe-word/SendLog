#!/bin/bash

sudo apt install -y python3 python3-pip
python3 --version
sleep 2
pip3 install requests

apt install cron
sudo systemctl start cron
sudo systemctl enable cron

wget 



