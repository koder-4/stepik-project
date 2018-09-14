#!/bin/sh
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/default /etc/nginx/sites-enabled/site.conf
sudo service nginx stop
sudo service nginx start
gunicorn hello:app --config etc/gunicorn.py
