from categorias.jsoncatego import crearjson


class Categoria(crearjson):
    def __init__(self, nom_categoria=''):
        super(Categoria, self).__init__('json/jsoncategoria.json')
        self.nom_categoria = nom_categoria
      

    def add(self, Categoria):
        self.lista.append(Categoria)

    def eliminar(self, Categoria):
        self.lista.remove(Categoria)

    def getCategoria(self, index):
        return self.lista[index]

    def modificar(self, index, Categoria):
        self.lista[index] = Categoria

  
    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nom_categoria.ljust(20)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Categoria(nom_categoria=x['nom_categoria']))
        self.lista = lista

    def getDictory(self):
        return {
            "nom_categoria": self.nom_categoria,
            
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
