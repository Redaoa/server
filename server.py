from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the server address and port
server_address = ('', 8000)  # '' means all available IPs, port 8000

# Create the HTTP server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Serving on port 8000...")
httpd.serve_forever()
e