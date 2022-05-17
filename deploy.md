# NastyLegacy Deployment Guide

## AWS

Using AWS, create an `EC2` instance

Create a Ubuntu Server

Connect to the server via `SSH` (PuTTy, WSL, etc.) or use the direct connection on AWS

```bash
# EXAMPLE:
ssh -i "legacy.pem" ubuntu@ec2-54-67-46-120.us-west-1.compute.amazonaws.com
```

## Setup

After connecting, begin setting up the web application

```bash
# add user
sudo adduser ubuntu sudo # sudo permissions
sudo adduser ubuntu adm # admin user
sudo adduser ubuntu www-data # for gunicorn service and nginx

# sign into user
su ubuntu # enter the passwowrd

# update
sudo apt-get update
sudo apt-get upgrade

# install python and nginx
sudo apt-get install python3-pip nginx git

# virtualenv
sudo pip install virtualenv
```

### Setup the GitHub Repo

```bash
# go to home directory
cd ~
git clone https://github.com/NastyLegacy/NastyLegacy.git # cloning repo to home directory

 # go to repo
ls -al
cd NastyLegacy
```

### Virtual Environment

```bash
virtualenv -p /usr/bin/python3 nasty
source nasty/bin/activate
```

### pip

```bash
pip install gunicorn # allows python to wrok with HTTP
pip install -r requirements.txt
```

### Python

Python should be working, start it now:

```bash
cd ~/NastyLegacy
python main.py

# test the connection
curl http://localhost:5000

# if working, deactivate the virtual environment
deactivate
```

## Gunicorn

### Changing Permissions

```bash
chown ubuntu:ubuntu /home/ubuntu/NastyLegacy
find /home/ubuntu/NastyLegacy -type d -exec chown ubuntu:ubuntu {} \;
find /home/ubuntu/NastyLegacy -type f -exec chown ubuntu:ubuntu {} \;
```

### Gunicorn Testing

Testing:

```bash
cd /home/ubuntu/NastyLegacy
nasty/bin/gunicorn --bind 0.0.0.0:5000 main:app

# test connection
curl http://localhost:5000/

# if successful, exit (^C)
deactivate
```

Setup Service File

```bash
sudo nano /etc/systemd/system/nasty.service # creating service file

# IN FILE:
[Unit]
Description=NastyLegacy Service File in Gunicorn
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/NastyLegacy
Environment="PATH=/home/ubuntu/NastyLegacy/nasty/bin"
ExecStart=/home/ubuntu/NastyLegacy/nasty/bin/gunicorn --workers 3 --bind unix:nasty.sock -m 007 main:app

[Install]
WantedBy=multi-user.target
```

## NginX

Begin setting up the NginX service

### NginX Config

Note:

- nastylegacy.cf = domain
- `52.9.190.46` = Elastic IP from AWS

```bash
sudo nano /etc/nginx/sites-available/nasty

# IN FILE:
server {
    listen 80;
    server_name nastylegacy.cf;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/NastyLegacy/nasty.sock;
    }
}
```

Restart:

```bash
sudo rm /etc/nginx/sites-available/default; sudo rm /etc/nginx/sites-enabled/default
sudo service nasty start
sudo systemctl enable nasty
sudo nginx -t
sudo nginx -s reload
sudo ufw allow 'Nginx Full'

# Check
sudo service nasty status 
journalctl -xe # check for errors
```

If service is running properly

```bash
sudo ln -s /etc/nginx/sites-available/nasty /etc/nginx/sites-enabled
sudo nginx -t # testing nginx config
sudo nginx -s reload

sudo service nginx restart

# pray it works
sudo service nginx status
journalctl -xe
```

## DNS

Use [freenom.com](https://www.freenom.com/) to establish a domain `nastylegacy.cf`

Use AWS Route53 to setup the routes to the Elastic IP of the web server

- IP of our public server: `52.9.190.46`

Go back to [freenom.com](https://www.freenom.com/) and click "Manage DNS"

- Add an A record pointing to the Elastic IP of our server
- Add another A record WWW pointing to the Elastic IP of our server

Think everything is working? Check:

[nastylegacy.cf](http://nastylegacy.cf)

If the page loads, begin setting up HTTPS

## HTTPS

```bash
sudo apt-get update
sudo apt install snapd
# updating snapd
sudo snap install core; sudo snap refresh core

# install Certbot (gives SSL Certificates for your website)
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Once installed
sudo certbot --nginx

# OUTPUTS
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx

Which names would you like to activate HTTPS for?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: nastylegacy.cf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel): 1

# if there are any more prompts, follow them accordingly
```

HTTPS should now be working

```bash
# QUICK TESTS
curl -k https://nastylegacy.cf # provides output
curl -k http://nastylegacy.cf # failure (insecure)

# can also open in browser and check for the 🔒
```

Now, the website is deployed!

> :tada: UNLESS IT ISN'T?

## Troubleshooting

Adding this because it wasn't working for some browsers initially

- Flush DNS: `ipconfig /flushdns`
- Go to Internet Properties -> Content -> Clear SSL state (Windows Only - Mac users you are on your own)
- Turn off your VPN ya monkey
- Re-install browser

> If the site does not load on any browser, go back and trace your steps because you messed up somewhere

## Updates

Create a script `update.sh` to auto-pull and update from the GitHub Repo

```bash
#!/bin/bash

function updates {
    # Update packages
    sudo apt-get update
    sudo apt-get install python3-pip nginx git
    sudo pip install virtualenv
    sudo pip install gunicorn
    sudo pip install -r requirements.txt
}

function github {
    # Github updates
    sudo git pull https://github.com/NastyEthan/NastyLegacy.git
    # I probably need to add to this
}

function svcupdate {
    # update service
    sudo systemctl restart nasty.service
    sudo nginx -s reload
    sudo systemctl restart nginx
}

function ubuntu {
    cd /home/ubuntu/NastyLegacy/
    updates
    github
    svcupdate
}

# bangers on bangers
nasty
```

### Using `update.sh`

```bash
ssh -i "legacy.pem" ubuntu@ec2-52-9-190-46.us-west-1.compute.amazonaws.com
sudo su # sudo perms, enter the password (nasty1234)
cd /home/ubuntu/NastyLegacy # go to git directory
bash update.sh # can also do "./update.sh"
# fix any dependency and git issues
# DONE
```
