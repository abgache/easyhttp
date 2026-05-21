from http.server import BaseHTTPRequestHandler, HTTPServer
from colorama import Fore, Style

def create_handler(code, body):
    class CustomHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Received request: {self.command} {self.path} from {self.client_address[0]}")
            self.send_response(code)
            self.end_headers()
            self.wfile.write(body.encode())
    return CustomHandler