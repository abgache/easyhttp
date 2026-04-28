#!/bin/bash
cd /usr/share
git clone https://github.com/abgache/easyhttp.git
cd easyhttp
pip install -r requirements.txt
chmod 555 /usr/share/easyhttp/main.py
cp /usr/share/easyhttp/bin/easyhttp /bin/easyhttp
cp /usr/share/easyhttp/bin/easyhttp-update /bin/easyhttp-update
chmod 555 /bin/easyhttp
chmod 555 /bin/easyhttp-update