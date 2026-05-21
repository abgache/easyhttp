from http.server import BaseHTTPRequestHandler

class LoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_request_data()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_POST(self):
        self.log_request_data()

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        print("=== BODY ===")
        print(post_data.decode(errors="ignore"))
        print("============")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_request_data(self):
        print("\n=== NEW REQUEST ===")

        # IP client
        client_ip = self.client_address[0]
        print(f"IP: {client_ip}")

        # Method + path
        print(f"Method: {self.command}")
        print(f"Path: {self.path}")

        # Headers
        print("=== HEADERS ===")
        for key, value in self.headers.items():
            print(f"{key}: {value}")

        # User-Agent spécifique
        user_agent = self.headers.get('User-Agent')
        print(f"\nUser-Agent: {user_agent}")

        print("=================\n")