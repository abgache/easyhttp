from http.server import BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def __init__(self, code, body, *args, **kwargs):
        self.code = code
        self.body = body
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(self.code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(self.body.encode())