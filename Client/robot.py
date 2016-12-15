import ev3dev.ev3 as ev3
import time

VELOCIDAD = 20


class ZumoRobot:
    def __init__(self):
        self.mFront = ev3.LargeMotor('outA')
        self.mRight = ev3.LargeMotor('outB')
        self.mLeft = ev3.LargeMotor('outC')
        self.touch_sensor = ev3.TouchSensor('in4')
        self.infrared_sensor = ev3.InfraredSensor('in2')
        self.color_sensor = ev3.ColorSensor('in1')
        self.tiempo_inicial = -1
        self.tiempo_regreso = -1

    def girar(self):
        self.mRight.run_forever(duty_cycle_sp=VELOCIDAD)
        self.mLeft.run_forever(duty_cycle_sp=VELOCIDAD)
        self.mFront.run_forever(duty_cycle_sp=VELOCIDAD)

    def stop(self):
        self.mRight.stop()
        self.mLeft.stop()
        self.mFront.stop()

    def avanzar(self):
        self.mRight.run_forever(duty_cycle_sp=-VELOCIDAD)
        self.mLeft.run_forever(duty_cycle_sp=VELOCIDAD)
        self.mFront.stop()

    def atras(self):
        self.mRight.run_forever(duty_cycle_sp=VELOCIDAD)
        self.mLeft.run_forever(duty_cycle_sp=-VELOCIDAD)
        self.mFront.stop()
