import http.server
import getip
import os

def serve():
    if os.sys.argv[1:]:
        port = int(os.sys.argv[1])
    else:
        port = 80

    server_address = (getip.address(4), port)
    http.server.SimpleHTTPRequestHandler.protocol_version = "HTTP/1.0"
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

    server = httpd.socket.getsockname()
    print(F"Serving HTTP on http://{server[0]+':'+str(server[1])}/...\n")
    httpd.serve_forever()
    pass


if __name__ == '__main__':
    try:
        serve()
    except Exception as e:
        print(e)
