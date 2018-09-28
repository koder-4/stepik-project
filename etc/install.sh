#!/bin/sh
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE stepik;"
sudo mysql -uroot -e "CREATE USER stepik IDENTIFIED BY 'password1';"
sudo mysql -uroot -e "GRANT ALL on stepik.* to stepik;"
sudo dpkg --purge python-django
sudo pip3 uninstall Django
sudo pip3 install Django==2.0 --upgrade
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/default /etc/nginx/sites-enabled/site.conf
sudo service nginx stop
sudo service nginx start
cd /home/box/web
gunicorn hello:app --config etc/gunicorn.py -D
