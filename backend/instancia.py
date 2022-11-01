class instancia:
    def __init__(self,idCliente, id,idConfiguracion,nombre,fechaInicio,estado,fechaFinal):
        self.idCliente=idCliente
        self.id=id
        self.idConfiguracion=idConfiguracion
        self.nombre=nombre
        self.fechaInicio=fechaInicio
        self.estado=estado
        self.fechaFinal=fechaFinal
    def getidCliente(self):
        return self.idCliente
    def getID(self):
        return self.id
    def getIDconfiguracion(self):
        return self.idConfiguracion
    def getNombre(self):
        return self.nombre
    def getFechainicio(self):
        return self.fechaInicio
    def getEstado(self):
        return self.estado
    def getFechafinal(self):
        return self.fechaFinal
    

    def setidCliente(self,idCliente):
        self.idCliente=idCliente
    def setID(self, id):
        self.id= id
    def setIDconfiguracion(self, idConfiguracion):
        self.idConfiguracion=idConfiguracion
    def setNombre(self,nombre):
        self.nombre=nombre
    def setFechainicio(self, fechaInicio):
        self.fechaInicio=fechaInicio
    def setEstado(self, estado):
        self.estado=estado
    def setFechafinal(self,Fechafinal):
        self.Fechafinal=Fechafinal