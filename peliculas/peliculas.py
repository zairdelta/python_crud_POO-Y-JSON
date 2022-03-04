from peliculas.jsonpeliculas import crearjson


class Pelicula(crearjson):
    def __init__(self, nom_pelicula='',categoria="", actor='', año=''):
        super(Pelicula, self).__init__('json/jsonPeliculas.json')
        self.nom_pelicula = nom_pelicula
        self.actor = actor
        self.año = año
        self.categoria = categoria

    def add(self, Pelicula):
        self.lista.append(Pelicula)

    def eliminar(self, Pelicula):
        self.lista.remove(Pelicula)

    def getPelicula(self,index):
        return self.lista[index]

    def modificar(self, index, Pelicula):
        self.lista[index] = Pelicula

  
    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nom_pelicula.ljust(20)+' \t\t'+self.categoria + '\t\t\t\t' + self.actor.ljust(20) + ' \t\t' + self.año

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Pelicula(nom_pelicula=x['nom_pelicula'],categoria=x["categoria"] ,actor=x['actor'], año=x["ano_estreno"]))
        self.lista = lista

    def getDictory(self):
        return {
            "nom_pelicula": self.nom_pelicula,
            "categoria": self.categoria,
            "actor": self.actor,
            "ano_estreno": self.año
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
