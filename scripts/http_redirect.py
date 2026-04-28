from http.server import BaseHTTPRequestHandler

class RedirectHandler(BaseHTTPRequestHandler):
    def __init__(self, redirect_url, *args, **kwargs):
        self.redirect_url = redirect_url
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(302)
        self.send_header('Location', self.redirect_url)
        self.end_headers()