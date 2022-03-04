from actores.actores import Actor
import os


class Interface():
    def __init__(self):
        self.lista = Actor()
        self.lista.toObjects()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoActor(self):
        p = Actor()
        p.nombre = input("Nombre del Actor:")
        p.apellido = input("Apellido del Actor:")
        p.edad = input("edad del Actor:")
        p.correo = input("correo del Actor:")
        return p

    def mostrarActor(self, lista=None):
        self.cls()
        print("\n\n" + "-" * 10 + "Datos de Actors" + "" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20) + '\t\t'+'Apellido'.ljust(20)+'\t\t' + 'edad'.ljust(20) + '\t\t'+'correo')
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")

    def buscarActor(self, code):
        mylista = [p for p in self.lista if p.nombre == code]
        self.mostrarActor(mylista)

    def getListaActor(self):
        return self.lista

    def modificarActor(self):
        id = input("Introduce ID:")
        id = int(id)
        p = self.lista.getlist()[id]
        cadena = input("Nombre del Actor:")
        if (len(cadena) > 0):
            p.nombre = cadena
        cadena = input("Apellido del Actor:")
        if (len(cadena) > 0):
            p.apellido = cadena
        cadena = input("edad del Actor:")
        if (len(cadena) > 0):
            p.edad = cadena
        cadena = input("correo del Actor:")
        if (len(cadena) > 0):
            p.correo = cadena
        self.lista.modificar(id, p)

    def eliminarActor(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getactor(id))
        self.lista.eliminar(self.lista.getactor(id))

    def menuActors(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menu Actors" + "-" * 10)
            print("1) Nuevo Actor")
            print("2) Modificar Actor")
            print("3) Eliminar Actor")
            print("4) Consultar Actor")
            print("5) Mostrar Actor")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.nuevoActor()
                self.lista.add(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarActor()
                self.modificarActor()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarActor()
                self.eliminarActor()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                codigo = input("dame el nombre:")
                self.buscarActor(codigo)
            elif (a == '5'):
                self.mostrarActor()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()