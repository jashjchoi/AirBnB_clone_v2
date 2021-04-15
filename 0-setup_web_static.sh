#!/usr/bin/env bash
# Install nginx and set up the web servers for web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  <title>TEST</title>
  </head>
  <body>
  <p>Holberton School is cool!</p>
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart