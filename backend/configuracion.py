class configuracion:
    def __init__(self,idcategoria,id, nombre,descripcion):
        self.idcategoria=idcategoria
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
    def getIDcategoria(self):
        return self.idcategoria
    def getID(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getDescripcion(self):
        return self.descripcion
    def setID(self,id):
        self.id=id
    def setNombre(self,nombre):
        self.nombre=nombre
    def setIDcategoria(self,idcategoria):
        self.idcategoria=idcategoria
    def setDescripcion(self,descripcion):
        self.descripcion=descripcion
