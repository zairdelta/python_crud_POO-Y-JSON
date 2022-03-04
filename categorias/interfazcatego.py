from categorias.categorias import Categoria
import os


class Interfacecategorias():
    def __init__(self):
        self.lista = Categoria()
        self.lista.toObjects()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoCategoria(self):
        p = Categoria()
        p.nom_categoria = input("Nombre del Categoria:")
       
        return p

    def mostrarCategoria(self, lista=None):
        self.cls()
        print("\n\n" + "-" * 10 + "Categorias" + "-" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre_categoria'.ljust(20) )
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")

    def buscarCategoria(self, code):
        mylista = [p for p in self.lista if p.nom_categorias == code]
        self.mostrarCategoria(mylista)

    def getListaCategoria(self):
        return self.lista

    def modificarCategoria(self):
        id = input("Introduce ID:")
        id = int(id)
        p = self.lista.getlist()[id]
        cadena = input("Nombre del Categoria:")
        if (len(cadena) > 0):
            p.nombre = cadena
       
        self.lista.modificar(id, p)

    def eliminarCategoria(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getCategoria(id))
        self.lista.eliminar(self.lista.getCategoria(id))

    def menuCategorias(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 30 + "Menu Categorias" + "-" * 30)
            print("1) Nuevo Categoria")
            print("2) Modificar Categoria")
            print("3) Eliminar Categoria")
            print("4) Consultar Categoria")
            print("5) Mostrar Categoria")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.nuevoCategoria()
                self.lista.add(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarCategoria()
                self.modificarCategoria()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarCategoria()
                self.eliminarCategoria()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                codigo = input("dame el nombre de categoria:")
                self.buscarCategoria(codigo)
            elif (a == '5'):
                self.mostrarCategoria()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()