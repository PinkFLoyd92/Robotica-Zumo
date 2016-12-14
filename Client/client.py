import socket
import sys
import time

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])


class mysocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self):
        self.sock.connect((HOST, PORT))
        print "Conectado a server {} Puerto: {}".format(HOST, PORT)

    def send(self, word=None):
        sent = self.sock.send(word)
        print "Sending data {}".format(word)


def main():
    client = mysocket()
    client.connect()  # nos conectamos al servidor
    while True:
        word = ""
        print "Intentando de enviar"
        word = raw_input("Ingrese una palabra a enviar...")
        client.send(word)


main()
