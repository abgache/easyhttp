#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root or with sudo."
  exit 1
fi
echo "Installing EasyHTTP..."
set -e
cd /usr/share
git clone https://github.com/abgache/easyhttp.git
cd easyhttp
chmod 555 /usr/share/easyhttp/main.py
install -m 755 /usr/share/easyhttp/bin/easyhttp /usr/local/bin/easyhttp
echo "Installation complete. You can now run 'easyhttp' from the command line."
#echo "Python requirements not installed automatically. Please run 'pip install -r /usr/share/easyhttp/requirements.txt' if you get any errors."