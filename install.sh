#!/bin/bash
sudo cd /usr/share
sudo git clone https://github.com/abgache/easyhttp.git
sudo cd easyhttp
sudo pip install -r requirements.txt
sudo chmod 555 /usr/share/easyhttp/main.py
sudo cp /usr/share/easyhttp/bin/easyhttp /bin/easyhttp
sudo cp /usr/share/easyhttp/bin/easyhttp-update /bin/easyhttp-update
sudo chmod 555 /bin/easyhttp
sudo chmod 555 /bin/easyhttp-update