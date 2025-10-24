#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

# Change to the directory where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    print(f"Starting server on port {PORT}")
    print(f"Serving files from: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    print(f"Access the AR marker at: http://localhost:{PORT}/ar-marker.html")
    print(f"Access the AR greeting card at: http://localhost:{PORT}/ar-greeting-card.html")
    print("Press Ctrl+C to stop the server")
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)
