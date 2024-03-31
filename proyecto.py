import os #Importamos esta libreria para hacer uso de la funcion os.sytem
import time  # Importamos esta libreria para hacer uso de la funcion time.sleep

def cursoTeorico ():
    print ("")
    
    
def clasesManejo ():
    print("")

def DictamenMedico (arrayInformacion):
    os.system ("cls")
    print ("Academica de Manejo CR\n")
    print("Si usted no cuenta con un dictamen Medico, nosotros de ofrecemos!!!")
    print ("¿Desea crear su dictamen medico con nosotros? (Y/N)")
    
    opcionCaracter = input ("\n>>> Opcion seleccionada: ")
    
    if opcionCaracter == "Y" : 
        print ("\nComplete la siguiente informacion\n")
        Nombrecompleto = input ("Nombre Completo: ")
        arrayInformacion.append(Nombrecompleto)
        id_user = input ("Cedula o Dimex o Pasaporte: ")
        arrayInformacion.append(id_user)
        natalidad = input ("Nacionalidad: ")
        arrayInformacion.append(natalidad)
        edad = input ("Edad: ")
        arrayInformacion.append(edad)
        ocupacion = input ("Ocupacion: ")
        arrayInformacion.append (ocupacion)
        estado_civil = input ("Estado Civil: ")
        arrayInformacion.append (estado_civil)
        correo_electronico = input ("Correo Electronico: ")
        arrayInformacion.append (correo_electronico)
        numero_telefono = input ("Numero Telefono: ")
        arrayInformacion.append (numero_telefono)
        direccion = input ("Direccion: ")
        arrayInformacion.append (direccion)
        estatura = input ("Estatura: ")
        arrayInformacion.append(estatura)
        peso = input ("Peso: ")
        arrayInformacion.append (peso)
        donante = input ("¿Desea ser donante? (Y/N): ")
        if donante == "Y" : 
            donante = "Donante"
            arrayInformacion.append(donante)
        else : 
            donante = "No Donante"
            arrayInformacion.append(donante)

        vision_lentes = input ("¿Usa lentes? (Y/N): ")
        if vision_lentes == "Y" : 
            vision_lentes = "Usa Lentes"
            arrayInformacion.append(vision_lentes)
        else: 
            vision_lentes = "No usa Lentes"
            arrayInformacion.append(vision_lentes) 
            
        print("\nHemos Terminado, gracias por la gestion\n")
        os.system ("pause")
        os.system ("cls")
    else: 
        os.system ("cls")
        return

def MenuAcademia (): 
    bienvenida = "Bienvenido Academia de Manejo CR"
    
    os.system("cls")
    print("\n"+bienvenida)
    
    #Aqui el numero se va registrar
    nombre_usuario = input ("\nIngrese su nombre: ")
    correo_electronico = input ("Ingrese su correo electronico: ")
    num_telefono = int (input ("Ingrese su numero de telefono: "))
    
    arrayinformacionUser = []
    
    #El sistema hace una breve espera antes de limpir consola
    time.sleep (0.5)
    os.system ("cls") #Esta funcion nos limpia consola
    
    #Creamos un menu interactivo
    opcion = 1

    while opcion != 4: 
        print ("Academica de Manejo CR\n")
        print("1. Curso Teorico"
            "\n2. Clases de Manejo"
            "\n3. Dictamen Medico"
            "\n4. Salir"
            )
        opcion = int (input ("\nSeleccionar una opcion: "))    
        
        if opcion == 1: 
            cursoTeorico ()
        elif opcion == 2:
            clasesManejo ()
        elif opcion == 3 :
            DictamenMedico (arrayinformacionUser)
    

if __name__ == "__main__":
    MenuAcademia()