# MDZ
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import time

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(open("test_page.html",'r').read()+open("comments.txt",'r').read()+open("test_page2.html",'r').read(), "utf-8"))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        comment = post_data.decode('utf-8').replace("+","%20")
        f = open("comments.txt", "a")
        f.write("<div id=\"space_box\"> &nbsp</div>\n"+"<div id=\"boxed\">"+urllib.parse.unquote(comment[4:])+"</div>\n")
        f.close()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(open("test_page.html",'r').read()+open("comments.txt",'r').read()+open("test_page2.html",'r').read(), "utf-8"))
if __name__ == "__main__": 
    open('comments.txt', 'w').close()
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")