#! Importamos la libreria desde el archivo rodi.py
import rodi
import time

#* Creo mi objeto y digo que es de la clase RoDI, es un  robotito
robot = rodi.RoDI()

while True:
    #* 'intenta' ejecutar estebloque de codigo
    try:
        #guardamos la lectura del metodo see en la variable llamada 'vista'
        vista = robot.see()
        #imprimo a que distancia esta lo que "ve" el rodi
        print(f"veo algo a {vista} cm")

        time.sleep(0.1)

    #* 'excepto' que pase esto 
    except KeyboardInterrupt:
        robot.pixel(230, 20, 10)
        break
