import socket
import sys
import time
from robot import ZumoRobot
from robot import VELOCIDAD

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])


class mysocket:

    def __init__(self, sock=None):
        self.data = ""
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

    def recibir(self):
        self.data = self.sock.recv(1024).decode()  # esperamos a que el server envie una respuesta.


def main():
    client = mysocket()
    client.connect()
    robot = ZumoRobot()
    while(robot.touch_sensor.value() == 0):
        print("Waiting....")
    robot.girar()
    while True:
        if int(robot.infrared_sensor.value()) <= 60:
            print("detectado obstaculo....")
            tiempo_start = time.time()
            while True:
                print("avanzando")
                robot.avanzar()
                if(robot.color_sensor.reflected_light_intensity() < 10):
                    print("linea negra...")
                    tiempo_regreso = time.time() - tiempo_start
                    robot.atras()
                    time.sleep(tiempo_regreso/2)
                    client.send("procesar_imagen")
                    robot.stop()  # detenemos el robot mientras intentamos procesar la imagen.
                    client.recibir()  # esperamos a que responda el servidor
                    while(self.data != "success"):
                        print "Esperando respuesta aceptable del servidor..."
                        client.send("procesar_imagen")
                        robot.avanzar()
                        time.sleep(tiempo_regreso/4)
                        robot.atras(tiempo_regreso/4)
                        time.sleep(tiempo_regreso/4)
                        client.recibir()
                    print "Se logro tomar la imagen. Respuesta del servidor: {}".format(client.data)
                    time.sleep(tiempo_regreso/2)
                    robot.girar()
                    break


main()
