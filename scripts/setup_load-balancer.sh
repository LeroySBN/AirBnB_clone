#!/usr/bin/env bash
# this script installs the HAproxy load balancer

# colors
green='\e[1;32m'
blue='\e[1;34m'
yellow='\e[1;33;1;40m'
reset='\033[0m'

echo -e "${blue}Running updates and checks...${reset}\n"

function install() {
	command -v "$1" &> /dev/null

	#shellcheck disable=SC2181
	if [ $? -ne 0 ]; then
		echo -e "Installing: ${yellow}$1${reset}\n"
		sudo apt-get install -y "$1" -qq
		echo -e "\n"
	else
		echo -e "${yellow}${1} is already installed.${reset}\n"
	fi
}

install haproxy

echo -e "${green}Finished installing ${yellow}$1${reset}\n"

echo -e "${blue}Setting up HAproxy...${reset}\n"

sudo cp /etc/haproxy/haproxy.cfg haproxy_cfg.backup

server_config=\
"
global
    log     /dev/log local0
    maxconn 1000
    user    haproxy
    group   haproxy
    tune.ssl.default-dh-param 2048

defaults
    log     global
    mode    http
    option  forwardfor
    option  httplog
    option  dontlognull
    timeout client  60s
    timeout connect  10s
    timeout server  10s
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http
    retries 3
    option  redispatch
    option  http-server-close

frontend www-http
    bind   *:80
    reqadd X-Forwarded-Proto:\ http
    default_backend www-backend
    redirect scheme https code 301 if !{ ssl_fc }


frontend www-https
   bind   *:443 ssl crt /home/ubuntu/haproxy.pem alpn h2,http/1.1
   reqadd X-Forwarded-Proto:\ https
   acl    letsencrypt-acl path_beg /.well-known/acme-challenge/
   use_backend letsencrypt-backend if letsencrypt-acl
   default_backend www-https

backend www-https
   balance  roundrobin
   redirect scheme https if !{ ssl_fc }
   server 100910-web-01 100.27.4.231:80 check
   server 100910-web-02 100.25.222.242:80 check

backend letsencrypt-backend
   server letsencrypt 127.0.0.1:71417
"

# shellcheck disable=SC2154
echo "$server_config" | sudo tee '/etc/haproxy/haproxy.cfg' > /dev/null

# enable haproxy to be started by init script
echo "ENABLED=1" | sudo tee '/etc/default/haproxy' > /dev/null

echo -e "${blue}Finished setting up HAproxy.${reset}"

# SETTING UP SSL
echo -e "${blue}Setting up SSL...${reset}\n"
install certbot
install python3-certbot-nginx

echo -e "${blue}Updating firewall...${reset}\n"
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo ufw reload
echo -e "${green}Finished updating firewall${reset}\n"

sudo certbot --nginx -d alphaziro.tech -d www.alphaziro.tech

sudo cat /etc/letsencrypt/live/alphaziro.tech/fullchain.pem /etc/letsencrypt/live/alphaziro.tech/privkey.pem | sudo tee '/etc/letsencrypt/live/alphaziro.tech/haproxy.pem' > /dev/null

# test the renewal process
sudo certbot renew --dry-run

echo -e "${green}Finished setting up SSL${reset}\n\n${blue}Done${reset}"

# FIREWALL SETUP
echo -e "${blue}Setting up firewall${reset}\n"
install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw enable
echo -e "${green}Finished setting up firewall.${reset}\n\n${blue}Done${reset}"
sudo ufw status
