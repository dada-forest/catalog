#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

git config --global user.name "Averill Cate, Jr"
git config --global user.email acatejr@gmail.com
apt update -y # && apt upgrade -y

# Add Docker's official GPG key:
apt-get update -y
apt-get install ca-certificates curl -y
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update -y

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
rm -rf /var/lib/apt/lists/
snap install tree
cat >> ~/.profile <<EOF
alias l='ls -lah --color=auto'
alias c='clear'
alias x='exit'
alias h='history'
alias dcu='docker compose up -d --build'
alias dcs='docker compose stop'
alias dsp='docker system prune -a'
alias dps='docker ps'
EOF
