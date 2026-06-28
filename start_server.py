#!/usr/bin/env python3
"""Simpele HTTP server voor de Regen Radar PWA.
Run dit script in de map waar index.html staat."""

import http.server
import socketserver
import socket

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS headers toestaan voor lokale ontwikkeling
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    ip = get_ip()
    print("=" * 50)
    print("🌧️  Vaneo's Regen Radar - Lokale Server")
    print("=" * 50)
    print(f"Server draait op:")
    print(f"  → Lokaal:   http://127.0.0.1:{PORT}")
    print(f"  → Netwerk:  http://{ip}:{PORT}")
    print("")
    print("Open Safari op je iPhone en ga naar:")
    print(f"  http://{ip}:{PORT}")
    print("")
    print("Druk Ctrl+C om te stoppen")
    print("=" * 50)

    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer gestopt.")
