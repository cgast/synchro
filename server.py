#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import json
from urlparse import urlparse, parse_qs

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
		global pageId
		if self.path.startswith('/setPage/'):
			pageId = self.path[9:]
			print 'setting page to ' + pageId
			self.send_response(200)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()
			self.wfile.write(json.dumps(pageId))
			return
		elif self.path.startswith('/getPage'):
			print 'current page is ' + pageId
			self.send_response(200)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()
			self.wfile.write(json.dumps(pageId))
			return
		else:
			return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

pageId = ""
Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()
