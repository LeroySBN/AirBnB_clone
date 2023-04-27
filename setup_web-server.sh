#!/usr/bin/env bash
# this script sets up the nginx web server

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

install nginx
sudo ufw allow 'Nginx HTTP'
sudo ufw reload
sudo ufw status
echo -e "${green}Finished installing ${yellow}$1${reset}\n"

sudo mkdir -p -m=755 /data/web_static/{releases/test,shared}

INDEX=\
"<html>
  <head>
  </head>
  <body>
    <h1>This is ALX SE!</h1>
  </body>
</html>"
echo -e "$INDEX" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

echo "Ceci n'est pas une page" | sudo tee "/var/www/html/404.html"  > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

SERVER_CONFIG=\
"# Custom server configuration
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;

        root /var/www/html;
        index index.html index.htm;

        server_name alphaziro.tech www.alphaziro.tech *.alphaziro.tech;

        location / {
				root /data/web_static/current/;
                index index.html index.htm;
				try_files \$uri \$uri/index.html \$uri.html =404;
        }
		
		location /hbnb_static/ {
                alias /data/web_static/current/;
        }

		error_page 404 /404.html;
		error_page 500 502 503 504 /50x.html;
}"
bash -c "echo -e '$SERVER_CONFIG' | sudo tee '/etc/nginx/sites-available/default' > /dev/null"

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

if [ "$(pgrep -c nginx)" -le 0 ]; then
	sudo service nginx start
else
	sudo service nginx restart
fi

exit 0
