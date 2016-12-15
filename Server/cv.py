import cv2
import numpy as np
# import math


def calcularContorno():
    cam = cv2.VideoCapture(0)
    while (True):
        booleano, frame = cam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        bajos = np.array([90, 50, 50])
        altos = np.array([110, 255, 255])  # valor maximo del color azul en H
        mask = cv2.inRange(hsv, bajos, altos)  # aplico filtro para azul
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(mask, kernel)
        erosion = cv2.erode(erosion, kernel)
        erosion = cv2.erode(erosion, kernel)
        dilatacion = cv2.dilate(erosion, kernel, iterations=2)
        # cv2.imshow('dilatacion', dilatacion)
        cont = frame.copy()
        moments = cv2.moments(dilatacion)  # saco lista de valores a la imagen filtrada mask
        area = moments['m00']  # m00 representa el area
        # lado = int(math.sqrt(area) / 20)  # determino un lado
        # contorno, jerarquia = cv2.findContours(dilatacion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contornos, _ = cv2.findContours(dilatacion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(cont, contornos, -1, (0, 255, 0), 2)
        maxArea = 0
        maxCont = None
        for i in range(0, len(contornos)):
            area = cv2.contourArea(contornos[i])
            if (area > maxArea):
                maxArea = area
                maxCont = contornos[i]

        if (maxArea > 0):  # dibujo un rectangulo alrededor del objeto
            x, y, w, h = cv2.boundingRect(maxCont)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        height, width, channels = frame.shape  # obtengo informacion sob re la imagen (ancho, alto, canales)
        cv2.line(frame, (width / 2 - 5, height / 2 - 5), (width / 2 + 5, height/2 + 5), (0, 125, 255), 2)
        cv2.line(frame, (width / 2 - 5, height / 2 + 5), (width / 2 + 5, height/2 - 5), (0, 125, 255), 2)
        cv2.rectangle(frame, (width / 2 - 2, height / 2 - 2), (width / 2 + 2, height/2 + 2), (255, 0, 255),
                      2)  # width/2,height/2 es el centro de la imagen
        # a = width / 2
        # b = height / 2
        # cv2.imshow("frame", frame)
        # cv2.imshow("mask", mask)
        # cv2.imshow('erosion', erosion)
        cv2.imshow('contorno', cont)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Se chequea si se presiona la tecla q (en la imagen)
            break

    cam.release()  # Cierra el driver de la camara
    cv2.destroyAllWindows()
