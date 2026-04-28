import argparse, socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from colorama import Fore, Style
# idk why I did that but why not ig
if __name__ == "__main__":
    from http_logger import LoggerHandler
    from http_redirect import RedirectHandler
elif __name__ == "scripts.scripts":
    from scripts.http_logger import LoggerHandler
    from scripts.http_redirect import RedirectHandler
else:
    print(f"{Fore.RED}[-]{Style.RESET_ALL} Error: Cannot determine import path for handlers")
    exit(1)

def banner(version):
    banner= r"""   ____              __ _________________ 
  / __/__ ____ __ __/ // /_  __/_  __/ _ \
 / _// _ `(_-</ // / _  / / /   / / / ___/
/___/\_,_/___/\_, /_//_/ /_/   /_/ /_/    
             /___/"""
    credit = f"\r             /___/{' ' * 16}By {Fore.BLUE}Abgache{Style.RESET_ALL}\n{' ' * 34}Version: {Fore.GREEN}{version}{Style.RESET_ALL}\n"
    print(banner, end="")
    print(credit)

def main():
    parser = argparse.ArgumentParser(description="The best HTTP server for pentesting and red teaming")
    parser.add_argument("-p", "--port", help="Port to listen on")
    parser.add_argument("-f","--file",help=f"Serve files from a directory",action="store_true")
    parser.add_argument("-l","--logger",help=f"Logger server",action="store_true")
    parser.add_argument("-r","--redirect",help=f"Redirect server")
    #parser.add_argument("--cc",help=f"Custom response code")

    args = parser.parse_args()
    port = args.port if args.port else 8000
    if args.logger:
        server = HTTPServer(("0.0.0.0", port), LoggerHandler)
    elif args.file:
        server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    elif args.redirect:
        server = HTTPServer(("0.0.0.0", port), RedirectHandler(args.redirect))
    else:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Please specify a mode: --file, --logger or --redirect")
        return
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Started HTTP server on port {port} in {'logger' if args.logger else 'file' if args.file else 'redirect'} mode")
    
    ips = socket.gethostbyname_ex(socket.gethostname())[2]
    urls = [f"http://{ip}:{port}" for ip in ips]
    print(f"{Fore.CYAN}[i]{Style.RESET_ALL} Server running on: {', '.join(urls)}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Server stopped by user")
        server.server_close()
    except Exception as e:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} An error occurred: {e}")
        server.server_close()