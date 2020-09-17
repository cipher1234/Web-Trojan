#!/bin/bash
apt-get update
apt-get install -y wget
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/my.cnf -O /etc/mysql/my.cnf
apt-get install -y unzip php5-gd
wget https://www.exploit-db.com/apps/f1f20b078f2a39a8e5e046fdc7eb4be7-Sentrifugo.zip -O /app/kiba.zip
unzip /app/kiba.zip -d /app
service apache2 start
chmod -R 777 /app/Sentrifugo_3.2
chmod  777 /app/Sentrifugo_3.2
bash /run.sh
