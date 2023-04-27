#!/usr/bin/env bash
# Configures ufw firewall to
# allow all outgoing traffic and
# block all incoming traffic except for ports 22(SSH), 443(HTTPS) and 80(HTTP).

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
		sudo apt update -y -qq && \
			sudo apt-get install -y "$1" -qq
		echo -e "\n"
	else
		echo -e "${yellow}${1} is already installed.${reset}\n"
	fi
}

echo -e "${green}Finished installing ${yellow}$1${reset}\n"

install ufw

echo -e "${blue}Setting up firewall${reset}\n"
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw enable
echo -e "${green}Finished setting up firewall.${reset}\n\n${blue}Done${reset}"
