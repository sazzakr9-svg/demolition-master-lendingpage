import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 3000), handler) as httpd:
    print("Serving on http://localhost:3000")
    httpd.serve_forever()
