#!/bin/bash
apt-get update
apt-get install -y wget
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/my.cnf -O /etc/mysql/my.cnf
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/create_mysql_admin_user.sh -O /create_mysql_admin_user.sh
apt-get install -y unzip php5-gd
wget http://192.168.225.95/kiba.zip -O /app/kiba.zip
unzip /app/kiba.zip -d /app
service apache2 start
chmod -R 777 /app/Sentrifugo_3.2
chmod  777 /app/Sentrifugo_3.2
bash /run.sh
