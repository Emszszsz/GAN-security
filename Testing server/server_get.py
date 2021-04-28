# MDZ
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import time
from http.cookies import SimpleCookie
import random
import sys
import os

sys.path.append(os.path.abspath('Network/'))
print("import")
import text_classification_network
print("after import")
hostName = "localhost"
serverPort = 8000

"""TODO:
generator zapisuje payloady w Network/workfile --> trzeba to włożyć do serwera"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == "/favicon.ico":
            self.send_response(500)
        else:
            if self.path == "/WIT_0.png":
                self.send_response(200)
                pic = open('Testing server/WIT_0.png', 'rb')
                self.wfile.write(pic.read())
            else:
                c = ""
                for i in range(0,21):
                    c += str(random.randint(0,9))
                self.send_response(200)
                if not self.headers.get('Cookie'):
                    self.send_header("Set-Cookie" , "session="+c)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(open("Testing server/test_page.html",'r').read()+open("Testing server/comments.txt",'r').read()+open("Testing server/test_page2.html",'r').read(), "utf-8"))      
    def do_POST(self):
        print("dostałem posta")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        commentery = post_data.decode('utf-8').replace("+","%20")
        f = open("Testing server/comment_to_check.txt", "w")
        f.write(urllib.parse.unquote(commentery[4:]))	
        f.close()
        file = open("Testing server/comment_to_check.txt",'r')
        comments = []
        comments.append(file.readlines())
        comment = comments[-1][-1]
        print("clasify?")
        print("")
        classy=text_classification_network.classify(f'{comment}', show_details=True)
        if(len(classy)==1):
                if(classy[0][0]=="safe"):
                        com = open("Testing Server/comments.txt",'a')
                        com.write("<div id=\"space_box\"> &nbsp</div>\n"+"<div id=\"boxed\">"+urllib.parse.unquote(commentery[4:])+"</div>\n")
                else:
                        alert = open("Testing Server/alerts.txt",'a')
                        alert.write("XSS alert!" + urllib.parse.unquote(commentery[4:]))
        else:
                if(float(classy[0][1])>float(classy[0][2])):
                        com = open("Testing Server/comments.txt",'a')
                        com.write("<div id=\"space_box\"> &nbsp</div>\n"+"<div id=\"boxed\">"+urllib.parse.unquote(commentery[4:])+"</div>\n")
                else:
                        alert = open("Testing Server/alerts.txt",'a')
                        alert.write("XSS alert!" + urllib.parse.unquote(commentery[4:]))
        #print(classy[0][1])
        #print(classy[1][1])
        file.close()
        print("classification ended?")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(open("Testing server/test_page.html",'r').read()+open("Testing server/comments.txt",'r').read()+open("Testing server/test_page2.html",'r').read(), "utf-8"))
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