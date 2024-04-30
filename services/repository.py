from models.articulo import Articulo

#Repository is an array of articles
class Repository:
    
    def __init__(self):
        self.database = []
        #Dummy data
        self.database.append(Articulo(id=1, titulo="Articulo 1", autor="Autor 1", contenido="Contenido 1", creado="2021-01-01", categoria="Categoria 1"))
        self.database.append(Articulo(id=2, titulo="Articulo 2", autor="Autor 2", contenido="Contenido 2", creado="2021-01-02", categoria="Categoria 2"))
        self.database.append(Articulo(id=3, titulo="Articulo 3", autor="Autor 3", contenido="Contenido 3", creado="2021-01-03", categoria="Categoria 3"))
        self.database.append(Articulo(id=4, titulo="Articulo 4", autor="Autor 4", contenido="Contenido 4", creado="2021-01-04", categoria="Categoria 4"))
        self.database.append(Articulo(id=5, titulo="Articulo 5", autor="Autor 5", contenido="Contenido 5", creado="2021-01-05", categoria="Categoria 5"))
    
    #Get all articles
    def get_articulos(self):
        return self.database
    
    #Get article by id
    def get_articulo(self, id):
        for articulo in self.database:
            if articulo.id == id:
                return articulo
        return None
    
    #Add article
    def add_articulo(self, articulo):
        self.database.append(articulo)
        return articulo
    
    #Update article
    def update_articulo(self, articulo):
        for i in range(len(self.database)):
            if self.database[i].id == articulo.id:
                self.database[i] = articulo
                return articulo
        return None
    
    #Delete article
    def delete_articulo(self, id):
        for i in range(len(self.database)):
            if self.database[i].id == id:
                articulo = self.database[i]
                del self.database[i]
                return articulo
        return None