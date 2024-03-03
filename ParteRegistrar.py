import os
import time 

bienvenida = "Bienvenido Academia de Manejo CR"

print("\n"+bienvenida.center(200, " "))

nombre_usuario = input ("Ingrese su nombre: ")
correo_electronico = input ("Ingrese su correo electronico: ")
num_telefono = int (input ("Ingrese su numero de telefono: "))

time.sleep (0.5)
os.system ("cls")

print ("Academica de Manejo CR".center(200," "))

opcion = 1

while opcion != 4: 
    print("1. Curso Teorico"
          "\n2. Clases de Manejo"
          "\n3. Dictamen Medico"
          "\n4. Salir"
          )
    opcion = int (input ("\nSeleccionar una opcion: "))    
    
    if opcion == 4: 
        print("\nGracias por usar nuestro programa\n")