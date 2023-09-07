#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
if ! dpkg -l | grep -q "nginx":
then
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello World" > /data/web_static/releases/test/index.html

# handle symblic link

if [ -L /data/web_static/current ] ;
then
    rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# set ownership

sudo chown -R ubuntu:ubuntu /data/

config="location /hbnb_static/ {\n   alias /data/web_static/current/;\n}\n"
sudo sed -i "/server_name _;/a $config" /etc/nginx/sites-available/default

service nginx restart
