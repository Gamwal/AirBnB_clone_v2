#!/usr/bin/env bash
# Bash script to install nginx and sets up for deployment

apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "AirBnB clone" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;
    rewrite ^/redirect_me https://www.fast.com permanent;

    error_page 404 /custom_404.html;
    location = /custom_404.html {
            root /var/www/html;
            internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
   }
}
" > /etc/nginx/sites-available/default

service nginx restart