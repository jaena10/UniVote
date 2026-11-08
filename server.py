import http.server
import socketserver
import os
from urllib.parse import urlparse

PORT = int(os.environ.get('PORT', 5000))

class UniVoteHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        clean_path = parsed.path.rstrip('/')

        # Health check endpoint for Render
        if clean_path in ['/health', '/healthz', '/ping']:
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"OK")
            return

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
    
    server_address = ("0.0.0.0", PORT)
    with http.server.ThreadingHTTPServer(server_address, UniVoteHandler) as httpd:
        print("==================================================")
        print("UniVote System - University of the Assumption")
        print(f"Server listening on http://0.0.0.0:{PORT}/")
        print(f"Student Portal: http://0.0.0.0:{PORT}/")
        print(f"Admin Console:  http://0.0.0.0:{PORT}/admin")
        print("==================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
