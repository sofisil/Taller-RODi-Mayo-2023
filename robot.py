#! Importamos la libreria desde el archivo rodi.py
import rodi
import time

#* Creo mi objeto y digo que es de la clase RoDI, es un  robotito
robot = rodi.RoDI()

#* Acceder a las acciones o funciones del robot (metodos) lo hago de la  siguiente manera

robot.move_forward()
time.sleep(1.5)
robot.move_stop()


