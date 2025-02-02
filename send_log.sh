#!/bin/bash

echo "*** X ***   $(curl -s ifconfig.me) $(date)" > current_logs.txt
echo -e "\n" >> current_logs.txt

echo "Hyperlane" >> current_logs.txt
docker logs --tail 25 hyperlane_op | grep -E "INFO"  >> current_logs.txt
echo -e "\n" >> current_logs.txt

echo "Glacier" >> current_logs.txt
docker logs --tail 3 glacier-verifier >> current_logs.txt 2>&1
echo -e "\n" >> current_logs.txt

echo "Elixir" >> current_logs.txt
docker logs --tail 30 elixir-main | grep -E "info"  >> current_logs.txt
echo -e "\n" >> current_logs.txt

echo "UniChain" >> current_logs.txt
docker logs  --tail 10 unichain-node-op-node-1 >> current_logs.txt 2>&1
echo -e "\n" >> current_logs.txt

echo "Sonaric" >> current_logs.txt
sonaric points >> current_logs.txt 2>&1
echo -e "\n" >> current_logs.txt

echo "Titan" >> current_logs.txt
docker logs --tail 7 titan  >> current_logs.txt 2>&1
echo -e "\n" >> current_logs.txt 

echo "Cysic" >> current_logs.txt
sudo journalctl -u cysic-verifier -n 2  >> current_logs.txt
echo -e "\n" >> current_logs.txt

echo "Initverse" >> current_logs.txt
sudo journalctl -u initverse-miner -n 2 >> current_logs.txt 
echo -e "\n" >> current_logs.txt 

# Запуск Python-скрипта
python3 send_logs.py
