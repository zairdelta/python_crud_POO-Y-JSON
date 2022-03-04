import os
from tkinter import W

from actores.interfazactores import Interface
from categorias.interfazcatego import Interfacecategorias
from peliculas.interfazpeliculas import Interfacepeliculas


class Main():
    def __init__(self):
        self.interfaceactor = Interface()
        self.interfacecategorias = Interfacecategorias()
        self.interfacepeliculas = Interfacepeliculas()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menuPrincipal(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 40 + "MENU" + "-" * 40)
            print("q) categorias")
            print("w) actores")
            print("e) peliculas")
            print("0) salir")
            a = input("Selecciona una opción: ")
            if (a.upper() == 'Q'):
                p = self.interfacecategorias.menuCategorias()
            elif (a.upper() == 'W'):
                p = self.interfaceactor.menuActors()
            elif (a.upper() == 'E'):
                p = self.interfacepeliculas.menupelicula()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()


if __name__ == '__main__':

    ip = Main()
    ip.menuPrincipal()
