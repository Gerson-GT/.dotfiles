#!/bin/bash

# sudo apt update
# sudo apt upgrade
# sudo apt autoremove

# sudo apt install curl

# echo "Instalando git"
# cd ~/
# sudo apt install libz-dev libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext cmake gcc
# mkdir tmp
# cd /tmp
# curl -o git.tar.gz https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.37.2.tar.gz
# tar -zxf git.tar.gz
# cd git-*
# make prefix=/usr/local all
# sudo make prefix=/usr/local install
# #exec bash --suegen errores
# git config --global user.name "Gerson-GT"
# git config --global user.email "gerson.lopez.com@gmail.com"
# git --version
# git config --list
# cd ~/.dotfile/

# echo "Instalando Neovim"
# sudo apt install -y vim neovim

# echo "Instalando Visual Studio Code"
# sudo apt update && sudo apt install software-properties-common apt-transport-https wget
# wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
# sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
# sudo apt install code

# echo #Instalar Docker"
# sudo apt-get install ca-certificates curl gnupg lsb-release
# sudo mkdir -p /etc/apt/keyrings
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# sudo apt-get update
# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin


echo "Todo bien! Hasta luego"
