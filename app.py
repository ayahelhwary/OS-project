from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from my Dockerized Python Web App!\n")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), HelloHandler)
    print("Server running on port 8080...")
    server.serve_forever()


