import BaseHTTPServer,CGIHTTPServer
import sys

def run(server_class=BaseHTTPServer.HTTPServer, \
        handler_class=CGIHTTPServer.CGIHTTPRequestHandler,port=80):
    server_address = ('', int(port))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
                  
if __name__ == '__main__':
    run(port=sys.argv[1])

