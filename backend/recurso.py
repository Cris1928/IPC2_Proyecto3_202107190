class recurso:
    def __init__(self,id, nombre,abreviatura,metrica,tipo,valorXhora):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.metrica=metrica
        self.tipo=tipo
        self.valorXhora=valorXhora
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getAbreviatura(self):
        return self.abreviatura
    def getMetrica(self):
        return self.metrica
    def getTipo(self):
        return self.tipo
    def getValorx(self):
        self.valorXhora
    def setId(self,id):
        self.id=id
    def setNombre(self,nombre):
        self.nombre=nombre
    def setAbreviatura(self,abreviatura):
        self.abreviatura=abreviatura
    def setMetrica(self,metrica):
        self.metrica=metrica
    def setTipo(self,tipo):
        self.tipo=tipo
    def setValorx(self,valorXhora):
        self.valorXhora=valorXhora
