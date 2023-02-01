class Pasajero:
    def __init__(self,nombre,apellido,destino,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.destino = destino
        self.dni = dni
    def __str__(self):
        return f"Nombre: {self.nombre}, {self.apellido} DNI: {self.dni} Destino: {self.destino}"
    def getnombre(self):
        return self.nombre
    def getapellido(self):
        return self.apellido
    def setNombre(self, pNombre):
        self.nombre = pNombre
    def setApellido(self, pApellido):
        self.apellido = pApellido
    def setDni(self, pDni):
        self.dni = pDni
    def setDestino(self, pDestino):
        self.destino = pDestino

#Funciones
def añadir():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    destino = input("Destino de viaje: ")
    dni = int(input("Ingresar DNI: "))
    pasajeroNuevo = Pasajero (nombre, apellido, destino, dni)
    listaPasajeros.append(pasajeroNuevo)
    
    #print(pasajeroNuevo)

def listar():
    print("")
    print("/////     Lista de pasajeros     /////")
    for indice in range (0, len(listaPasajeros)):
        print(f"{indice + 1} - {listaPasajeros[indice]}")
    print("")

def eliminar():
    listar()
    indice = int(input("Ingresar pasajero que quiere eliminar: "))
    print(f"Seguro/a que quieres borrar a {listaPasajeros[indice -1].getnombre()} {listaPasajeros[indice -1].getapellido()}")
    respuesta = input("S- eliminar N- No eliminar: ")
    if respuesta == "s":
        listaPasajeros.remove(listaPasajeros[indice -1])
        print("Pasajero Eliminado...")
    elif respuesta == "n":
        print("Volviendo al menú...")
    else:
        print("Opción incorrecta...")

def modificar():
    listar()
    indice = int(input("Ingresar pasajero que quiere modificar: "))
    nombre = input("Ingresar nuevo nombre: ")
    listaPasajeros[indice -1].setNombre(nombre)
    apellido = input("Ingresar nuevo apellido: ")
    listaPasajeros[indice -1].setApellido(apellido)
    dni = input("Ingresar nuevo DNI: ")
    listaPasajeros[indice -1].setDni(dni)
    destino = input("Ingresar nuevo destino: ")
    listaPasajeros[indice -1].setDestino(destino)
    print("Usuario Modificado...")

# Inicio del Crud
listaPasajeros = []
opcion = ""
while opcion != "5" :
    print("/////     Menú de pasajeros    /////")
    print("[1]. Añadir pasajero")
    print("[2]. Modificar pasajero")
    print("[3]. Listar pasajeros")
    print("[4]. Eliminar pasajeros")
    print("[5]. Exit")
    opcion = input("Selecciona una opción: ")
    if opcion == "5":
        print("Saliendo...")
    elif opcion == "1":
        añadir()
    elif opcion == "2":
        modificar()
    elif opcion == "3":
        listar()
    elif opcion == "4":
        eliminar()
    else:
        print("Error de elección...")
