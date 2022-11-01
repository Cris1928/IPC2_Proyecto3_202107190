class categoria:
    def __init__(self,id, nombre,descripcion,cargaTrabajo):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.cargaTrabajo=cargaTrabajo
        self.configuraciones=[]
    def getID(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getDescripcion(self):
        return self.descripcion
    def getCargaTrabajo(self):
        return self.cargaTrabajo
    def setID(self,id):
        self.id=id
    def setNombre(self,nombre):
        self.nombre=nombre
    def setDescripcion(self,descripcion):
        self.descripcion=descripcion
    def setCargaTrabajo(self,cargaTrabajo):
        self.cargaTrabajo=cargaTrabajo
