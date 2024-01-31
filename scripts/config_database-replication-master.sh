#!/usr/bin/env bash
# sets up the master mysql database

# Allow connection from slaves database server
sudo ufw allow from "$1" to any port 3306

CONFIG=\
"[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
# By default we only accept connections from localhost
#bind-address   = 127.0.0.1
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

server-id       = 1
# Enable binary logging
log_bin         = /var/log/mysql/mysql-bin.log
# Database to replicate
binlog_do_db    = target_database"

bash -c "echo -e '$CONFIG' | sudo tee '/etc/mysql/mysql.conf.d/mysqld.cnf' > /dev/null"

sudo systemctl restart mysql
