usuarios ={}

def validar_contraseña(contraseña):
     if len(contraseña) < 8:
       return False
     if not any(c.isalpha()for c in contraseña):
      return False
     if  not any (c.isdigit()for c in contraseña):
      return False
     if " " in contraseña:
         return False
     return True

def ingresar_usuario():
     nombre = input("Ingrese nombre de usuario:")
     if nombre in usuarios:
        print("El nombre de usuario ya existe.")
        return
     
     while True:
        sexo = input("Ingrese sexo (F o M):").upper()
        if sexo in ['F','M']:
           break
        else:
           print("Debe ingresar F o M solamente.Intente de nuevo.")

     while True:
        contraseña =input("Ingrese contraseña:")
        if validar_contraseña(contraseña):
            break
        else:
           print("Contraseña invalida.Debe tener minimo 8 caracteres,al menos una letra, un numero  sin espacios.")

     usuarios[nombre] = {"sexo":sexo,"contraseña":contraseña}
     print("Usuario ingresado correctamente.")

def buscar_usuario():
    nombre = input("Ingrese nombre de usuario a buscar:")
    if nombre in usuarios:
       print("Sexo:",usuarios[nombre]["sexo"])
       print("Contraseña:",usuarios[nombre]["contraseña"])
    else:
        print("Usuario no se encuentra.")

def eliminar_usuario():
    nombre = input("Ingrese nombre de usuario a eliminar:")
    if nombre in usuarios:
       del usuarios[nombre]  
       print("Usuario eliminado.")  
    else:
        print("No se pudo eliminar usuario.")
def menu():
   while True:
       print("/nMenu principal")
       print("1.Ingresar usuario")
       print("2.Buscar usuario")
       print("3.Eliminar usuario")
       print("4.Salir")

       opcion = input("Ingrese opcion:")

       if opcion == "1":
           ingresar_usuario()
       elif opcion == "2":
           buscar_usuario()
       elif opcion == "3":
           eliminar_usuario()
       elif opcion =="4":
           print("Saliendo del programa.")
           break
       else:
          print("Debe seleccionar una opcion valida.")

#ejecutar el menu
menu()




    