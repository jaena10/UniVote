import http.server
import socketserver
import os
from urllib.parse import urlparse

PORT = 5000

class UniVoteHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        clean_path = parsed.path.rstrip('/')

        # Normalize admin routes
        if clean_path in ['/admin', '/adminweb', '/adminweb.html', '/admin.html']:
            self.path = '/templates/adminweb.html'
        # Normalize student routes
        elif clean_path in ['', '/', '/student', '/studentweb', '/studentweb.html', '/student.html']:
            self.path = '/templates/studentweb.html'

        return super().do_GET()

if __name__ == '__main__':
    # Set the working directory to the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), UniVoteHandler) as httpd:
        print("==================================================")
        print(f"UniVote Server running at http://127.0.0.1:{PORT}/")
        print(f"Student Portal: http://127.0.0.1:{PORT}/")
        print(f"Admin Console:  http://127.0.0.1:{PORT}/admin")
        print("Press Ctrl + C to stop.")
        print("==================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
