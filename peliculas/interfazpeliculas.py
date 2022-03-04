from peliculas.peliculas import Pelicula
import os


class Interfacepeliculas():
    def __init__(self):
        self.lista = Pelicula()
        self.lista.toObjects()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevopelicula(self):
        p = Pelicula()
        p.nom_pelicula = input("Nombre de la pelicula:")
        p.categoria = input("categoria de la pelicula:")
        p.actor = input("actor de la pelicula:")
        p.año = input("año de publicacion de pelicula:")
        return p

    def mostrarpelicula(self, lista=None):
        self.cls()
        print("\n\n" + "*" * 30 + "Datos de pelicula" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre_pelicula'.ljust(20) + '\t\t'+'categoria'.ljust(20)+'\t\t' + 'actor'.ljust(20) + '\t\t' +' ano_estreno')
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")

    def buscarpelicula(self, code):
        mylista = [p for p in self.lista if p.nom_pelicula == code]
        self.mostrarpelicula(mylista)

    def getListapelicula(self):
        return self.lista

    def modificarpelicula(self):
        id = input("Introduce ID:")
        id = int(id)
        p = self.lista.getlist()[id]
        cadena = input("Nombre del pelicula:")
        if (len(cadena) > 0):
            p.nom_pelicula = cadena
        cadena = input("Apellido del pelicula:")
        if (len(cadena) > 0):
            p.categoria = cadena
        cadena = input("edad del pelicula:")
        if (len(cadena) > 0):
            p.actor = cadena
        cadena = input("Direccion del pelicula:")
        if (len(cadena) > 0):
            p.año = cadena
        self.lista.modificar(id, p)

    def eliminarpelicula(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getPelicula(id))
        self.lista.eliminar(self.lista.getPelicula(id))

    def menupelicula(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 30 + "Menu pelicula" + "-" * 30)
            print("1) Nuevo pelicula")
            print("2) Modificar pelicula")
            print("3) Eliminar pelicula")
            print("4) Consultar pelicula")
            print("5) Mostrar pelicula")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.nuevopelicula()
                self.lista.add(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarpelicula()
                self.modificarpelicula()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarpelicula()
                self.eliminarpelicula()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                codigo = input("dame el nombre:")
                self.buscarpelicula(codigo)
            elif (a == '5'):
                self.mostrarpelicula()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()