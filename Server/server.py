import sys
import time
import SocketServer
from cv import calcularContorno


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.procesado = False
        self.data = ""
        print "Conectado ev3"
        while(True):
            self.data = str(self.request.recv(1024).strip())
            print "Datos: ... {}".format(self.data)
            if(self.data == "procesar_imagen"):
                self.procesado = calcularContorno()
                if self.procesado is True:
                    self.request.sendall("success")
                else:
                    self.request.sendall("mal_procesamiento")


if __name__ == "__main__":
    HOST, PORT = str(sys.argv[1]), int(sys.argv[2])
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # corre el servidor por siempre a
    # menos que se termine el programa con Ctrl-c
    server.serve_forever()

main()
