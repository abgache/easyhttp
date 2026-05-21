from http.server import BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def __init__(self, custom_code, custom_body, *args, **kwargs):
        self.custom_code = custom_code
        self.custom_body = custom_body
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(self.custom_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.custom_body.encode())

    def do_GET(self):
        self.send_response(302)
        self.send_header('Location', self.redirect_url)
        self.end_headers()