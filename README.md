# EasyHTTP  
## The best HTTP server for pentesting and red teaming  

### Version: ``1.0.0``  

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/) 

# What is it?  
It is a simple python-made HTTP server, for logging requests, file acces or redirection.  
  
# How to use it?
**Download:**    
Just run ``install.sh`` with sudo privileges.  
**Usage:**  
```bash
age: main.py [-h] [-p PORT] [-f] [-l] [-r REDIRECT_LOCATION]
```
**options:**  
> -h, --help            show this help message and exit  
> -p PORT, --port PORT  Port to listen on  
> -f, --file            Serve files from a directory  
> -l, --logger          Logger server  
> -r REDIRECT, --redirect REDIRECT  
>                       Redirect server  
**Update:**  
```bash  
sudo easyhttp-update  
``` 