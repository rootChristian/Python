#coding:utf-8

import http.server
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())  

host = ''
port = ****

address = (host, port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print (f"Server running on the port {port}")

httpd.serve_forever()

'''
import http.server
import socketserver

host = ''
port = 80

address = ('', port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print (f"Server running on the port {port}")

httpd.serve_forever()
'''
