import ev3dev.ev3 as ev3
import time

mFront = ev3.LargeMotor('outA')
mRight = ev3.LargeMotor('outB')
mLeft = ev3.LargeMotor('outC')

touch_sensor = ev3.TouchSensor('in4')
infrared_sensor = ev3.InfraredSensor('in2')
color_sensor = ev3.ColorSensor('in1')

velocidad = 20
tiempo_inicial = -1
tiempo_regreso = -1


def girar():
    mRight.run_forever(duty_cycle_sp=velocidad)
    mLeft.run_forever(duty_cycle_sp=velocidad)
    mFront.run_forever(duty_cycle_sp=velocidad)


def stop():
    mRight.stop()
    mLeft.stop()
    mFront.stop()


def avanzar():
    mRight.run_forever(duty_cycle_sp=-velocidad)
    mLeft.run_forever(duty_cycle_sp=velocidad)
    mFront.stop()


def atras():
    mRight.run_forever(duty_cycle_sp=velocidad)
    mLeft.run_forever(duty_cycle_sp=-velocidad)
    mFront.stop()


def main():
    while(touch_sensor.value() == 0):
        print("Waiting....")
    girar()
    while True:
        if int(infrared_sensor.value()) <= 60:
            print("detectado obstaculo....")
            tiempo_start = time.time()
            while True:
                print("avanzando")
                avanzar()
                if(color_sensor.reflected_light_intensity() < 10):
                    print("linea negra...")
                    tiempo_regreso = time.time() - tiempo_start
                    atras()
                    time.sleep(tiempo_regreso)
                    girar()
                    break

main()
