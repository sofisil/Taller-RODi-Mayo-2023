#! Importamos la libreria desde el archivo rodi.py
import rodi
import time

#* Creo mi objeto y digo que es de la clase RoDI, es un  robotito
robot = rodi.RoDI()

while True:
    try:
        #*sensor de lineas ( el de abajo)
        lineas = robot.sense()
        #* que tan distante esta algo del rodi, sensor del frente
        vista = robot.see()
        time.sleep(1)
        valor_1 = lineas[0]
        print(f"este estel primer valor {valor_1}")
        valor_2 = lineas[1]
        print(f"este estel segundo valor {valor_2}")


        if 20 >= vista >= 5 or valor_1 >= 900:
            robot.move_left()
            time.sleep(0.5)
            robot.move_forward()

        elif vista < 5:
            robot.move_backward()
            time.sleep(1)
            robot.move_stop()

    except KeyboardInterrupt:
        robot.move_stop()
        robot.pixel(240,0.20)
        break