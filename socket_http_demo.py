# Simple HTTPsERVER

import SocketServer
import SimpleHTTPServer
import BaseHTTPServer
import CGIHTTPServer
import os
import stat

os.chmod("./cgi-bin/post.py", stat.S_IRWXU | stat.S_IRWXG | stat.S_IXOTH)

HOST = ''
PORT = 8000

# Create the server,
# # SimpleHTTPRequestHander is pre-defined handler in SimpleHTTPServer package, but it cannot handler post
# server = SocketServer.TCPServer((HOST, PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
server = BaseHTTPServer.HTTPServer((HOST, PORT), CGIHTTPServer.CGIHTTPRequestHandler)
# Start the server
server.serve_forever()
