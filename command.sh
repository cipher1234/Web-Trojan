#!/bin/bash
apt-get update
apt-get install -y wget
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/my.cnf -O /etc/mysql/my.cnf
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/create_mysql_admin_user.sh -O /create_mysql_admin_user.sh
apt-get install -y unzip php5-gd
wget https://www.exploit-db.com/apps/f1f20b078f2a39a8e5e046fdc7eb4be7-Sentrifugo.zip -O /app/kiba.zip
unzip /app/kiba.zip -d /app
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/success.php -O /app/Sentrifugo_3.2/success.php
service apache2 start
chmod -R 777 /app/Sentrifugo_3.2
chmod  777 /app/Sentrifugo_3.2
mysql_install_db > /dev/null 2>&1
service mysql start
service apache2 start
bash /create_mysql_admin_user.sh
apt-get install -y python-pip
pip install requests
wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/kiba.py -O kiba.py
python /kiba.py > kiba.txt
#cat /kiba.txt | grep "Username"
#cat /kiba.txt | grep "Password"
echo "Username:empp0001"
echo "Password:example"
mysql -uroot -e "update sentry.main_users set emppassword=md5('example') where id=1;"
bash
