# EasyHTTP  
## The best HTTP server for pentesting and red teaming  

### Version: ``1.3.0``  

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/) 

# What is it?  
It is a simple python-made HTTP server, for logging requests, file acces or redirection.  
  
# How to use it?
**Download:**    
Just run ``install.sh`` with sudo privileges.  
One-liner:  
```bash
curl -fsSL https://raw.githubusercontent.com/abgache/easyhttp/main/install.sh | bash
```
**Usage:**  
```bash
age: main.py [-h] [-p PORT] [-f] [-l] [-r REDIRECT_LOCATION]
```
**options:**  
>  -h, --help            show this help message and exit  
>  -p PORT, --port PORT  Port to listen on  
>  -f, --file            Serve files from a directory  
>  -l, --logger          Logger server  
>  -r REDIRECT, --redirect REDIRECT  
>                        Redirect server  
>  -c CUSTOM, --custom CUSTOM  
>                        Custom response code  
>  --body BODY           Custom body, only used with --custom  
>  --lifetime LIFETIME, -t LIFETIME  
>                        Server timeout in seconds (Default: No timeout)  
>  --update              Update EasyHTTP  
  
**Update:**  
```bash  
sudo easyhttp --update 
``` 