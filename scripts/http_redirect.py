from http.server import BaseHTTPRequestHandler

def create_handler(redirect_url):
    class RedirectHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            print(f"")
            self.send_response(302)
            self.send_header('Location', redirect_url)
            self.end_headers()

        def log_message(self, format, *args):
            return  # optionnel: supprime les logs console

    return RedirectHandler