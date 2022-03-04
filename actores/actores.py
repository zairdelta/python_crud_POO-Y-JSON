from actores.jsonactores import crearjson


class Actor(crearjson):
    def __init__(self, nombre='',apellido="", edad='', correo=''):
        super(Actor, self).__init__('json/jsonactores.json')
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.correo = correo

    def add(self, Actor):
        self.lista.append(Actor)

    def eliminar(self, Actor):
        self.lista.remove(Actor)

    def getactor(self,index):
        return self.lista[index]

    def modificar(self, index, Actor):
        self.lista[index] = Actor

  
    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nombre.ljust(20)+' \t\t'+self.apellido.ljust(20) + '\t\t\t\t' + self.edad.ljust(20) + ' \t\t' + self.correo

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Actor(nombre=x['nombre'],apellido=x["apellido"] ,edad=x['edad'], correo=x["correo"]))
        self.lista = lista

    def getDictory(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "correo": self.correo
        }


    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        if self.__idx__ < len(self.lista):
            x = self.lista[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration


   