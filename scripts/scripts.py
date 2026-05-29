import argparse, socket, threading, time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from colorama import Fore, Style
# idk why I did that but why not ig
if __name__ == "__main__":
    from http_logger import LoggerHandler
    from http_redirect import RedirectHandler
    from http_custom import CustomHandler
elif __name__ == "scripts.scripts":
    from scripts.http_logger import LoggerHandler
    from scripts.http_redirect import create_handler as create_redirect_handler
    from scripts.http_custom import create_handler as create_custom_handler
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

def parse():
    parser = argparse.ArgumentParser(description="The best HTTP server for pentesting and red teaming")
    parser.add_argument("-p", "--port", help="Port to listen on")
    parser.add_argument("-f","--file",help=f"Serve files from a directory",action="store_true")
    parser.add_argument("-l","--logger",help=f"Logger server",action="store_true")
    parser.add_argument("-r","--redirect",help=f"Redirect server")
    parser.add_argument("-c","--custom",help=f"Custom response code")
    parser.add_argument("--body",help=f"Custom body, only used with --custom")
    parser.add_argument("--lifetime", "-t",help=f"Server timeout in seconds (Default: No timeout)",type=int)
    return parser.parse_args()

def main():
    args = parse()
    port = args.port if args.port else 8000
    try:
        port = int(port)
        if port < 1 or port > 65535:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Port number must be between 1 and 65535, actually got {port}")
            exit(6)
    except ValueError as ve:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Invalid port number: {ve}")
        exit(5)
    
    if args.body and not args.custom:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} --body can only be used with --custom")
        exit(7)

    if args.logger:
        server = HTTPServer(("0.0.0.0", port), LoggerHandler)
    elif args.file:
        server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    elif args.redirect:
        server = HTTPServer(("0.0.0.0", port), create_redirect_handler(args.redirect))
    elif args.custom:
        # args.custom = code | args.body = body
        no_body_answers = [100, 101, 102, 204, 205, 304]
        if args.body and int(args.custom) in no_body_answers:
            print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Response code {args.custom} does not support a body, ignoring --body")
            args.body = None
        server = HTTPServer(("0.0.0.0", port), create_custom_handler(int(args.custom), args.body))
    else:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Please specify a mode: --file, --logger or --redirect")
        exit(4)
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Started HTTP server on port {port} in {'logger' if args.logger else 'file' if args.file else 'redirect'} mode, Ctrl+C to stop")
    
    ips = socket.gethostbyname_ex(socket.gethostname())[2]
    urls = [f"http://{ip}:{port}" for ip in ips]
    print(f"{Fore.CYAN}[i]{Style.RESET_ALL} Server running on: {', '.join(urls)}")


    try:
        if args.lifetime:
            if args.lifetime < 1:
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Lifetime must be a positive integer, actually got {args.lifetime}")
                exit(8)
            def shutdown_server():
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Lifetime reached ({args.lifetime}s), shutting down server...")
                server.shutdown()
                exit(0)
            print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Server will automatically stop after {args.lifetime} seconds")
            timer = threading.Timer(args.lifetime, shutdown_server)
            timer.daemon = True
            timer.start()
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\r{Fore.RED}[-]{Style.RESET_ALL} Server stopped by user")
        server.server_close()
    except Exception as e:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} An error occurred: {e}")
        server.server_close()