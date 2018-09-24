#!/bin/sh
sudo dpkg --purge python-django
sudo pip3 uninstal Django
sudo pip3 install Django==2.0 --update
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/default /etc/nginx/sites-enabled/site.conf
sudo service nginx stop
sudo service nginx start
cd /home/box/web
gunicorn hello:app --config etc/gunicorn.py
