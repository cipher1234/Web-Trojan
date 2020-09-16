#!/bin/bash

VOLUME_HOME="/var/lib/mysql"

sed -ri -e "s/^upload_max_filesize.*/upload_max_filesize = ${PHP_UPLOAD_MAX_FILESIZE}/" \
    -e "s/^post_max_size.*/post_max_size = ${PHP_POST_MAX_SIZE}/" /etc/php5/apache2/php.ini
if [[ ! -d $VOLUME_HOME/mysql ]]; then
    echo "=> An empty or uninitialized MySQL volume is detected in $VOLUME_HOME"
    echo "=> Installing MySQL ..."
    apt-get update
    apt-get install wget
    rm /etc/mysql/my.cnf
    service apache2 start
    wget https://raw.githubusercontent.com/cipher1234/Web-Trojan/master/my.cnf -O /etc/mysql/my.cnf
    mysql_install_db > /dev/null 2>&1
    echo "=> Done!"  
    sleep 5
    mysql -uroot -e "CREATE USER 'user'@'%' IDENTIFIED BY 'password'"
    mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'user'@'password' WITH GRANT OPTION"
else
    echo "=> Using an existing volume of MySQL"
fi

exec supervisord -n
