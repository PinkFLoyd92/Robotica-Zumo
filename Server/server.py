import sys
import time
import SocketServer


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = ""
        # self.request is the TCP socket connected to the client
        print "Nuevo cliente"
        while(self.data != "out"):
            self.data = str(self.request.recv(1024).strip())
            if(self.data == ""):
                print "conexion interrumpida..."
            elif(self.data != "out"):
                print "Datos: ... {}".format(self.data)


if __name__ == "__main__":
    HOST, PORT = str(sys.argv[1]), int(sys.argv[2])
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # corre el servidor por siempre a
    # menos que se termine el programa con Ctrl-c
    server.serve_forever()
