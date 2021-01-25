
"""
Very simple HTTP server in python (Updated for Python 3.7)
Usage:
    ./dummy-web-server.py -h
    ./dummy-web-server.py -l localhost -p 8000
Send a GET request:
    curl http://localhost:8000
Send a HEAD request:
    curl -I http://localhost:8000
Send a POST request:
    curl -d "foo=bar&bin=baz" http://localhost:8000
"""
from pool import SlavePool
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import re
import urllib.parse


class Server(BaseHTTPRequestHandler):
    mypool = SlavePool(10)
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        regex_text = "^\/get_slaves[?]amount[=][0-9]+[&]duration[=][0-9]+" #regex expresion
        if re.match(regex_text, self.path):
            self._set_headers()
            self.wfile.write(json.dumps("correct get request ").encode())
            print(urllib.parse.parse_qs(self.path[12:]))
            request_obg = urllib.parse.parse_qs(self.path[12:])
            amount = re.sub("[^0-9]", "", str(request_obg['amount']))
            duration = re.sub("[^0-9]", "", str(request_obg['duration']))
            self.wfile.write(json.dumps("you have requested: "+ amount+" slaves for a period of: "+duration+" seconds").encode())
            self.wfile.write(json.dumps(self.mypool.request_slaves(int(amount), int(duration))).encode())
        else:
            self._set_headers()
            self.wfile.write(json.dumps("wrong get request try: /get_slaves?amount=SLAVE_#&duration=WORKING_TIME").encode())

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read(length))

        # add a property to the object, just to mess with data
        message['received'] = 'ok'

        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message))


def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
'''
#server with HtML Page
from pool import SlavePool
import json
import re
import urllib.parse
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    mypool = SlavePool(10)

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        regex_text = "^\/get_slaves[?]amount[=][0-9]+[&]duration[=][0-9]+" #regex expresion
        if re.match(regex_text, self.path):
            self._set_headers()
            self.wfile.write(self._html("correct get request "))
            print(urllib.parse.parse_qs(self.path[12:]))
            request_obg = urllib.parse.parse_qs(self.path[12:])
            amount = re.sub("[^0-9]", "", str(request_obg['amount']))
            duration = re.sub("[^0-9]", "", str(request_obg['duration']))
            self.wfile.write(self._html("you have requested: "+ amount+" slaves for a period of: "+duration+" seconds"))
            self.wfile.write(json.dumps(self.mypool.request_slaves(int(amount), int(duration))).encode())
        else:
            self._set_headers()
            self.wfile.write(self._html("wrong get request try: /get_slaves?amount=SLAVE_#&duration=WORKING_TIME"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        #self.wfile.write(self._html("POST!"))
        self.wfile.write(json.dumps("POST!").encode())


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
'''
'''
    my test 
    if __name__ == '__main__':
        duration = 2

        slave1 = Slave("slave1", "28.235.193.228")
        slave1.tostring()
        slave1.working_time(duration)
        print(str(slave1.isWorking))
        slave1.tostring()
        print(str(slave1.isWorking))
        time.sleep(duration+3)
        print(str(slave1.isWorking))



        my_pool = SlavePool(10)
        #my_pool.tostring()
        my_pool.request_slaves(12, duration)
        my_pool.request_slaves(6, duration + 2)
        my_pool.request_slaves(4, duration - 1)
        my_pool.request_slaves(1, duration + 4)
'''
