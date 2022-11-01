from flask import  jsonify
class cliente:
    def __init__(self, nit, nombre, usuario,clave,direccion,correo_electronico):
        self.nit=nit
        self.nombre=nombre
        self.usuario=usuario
        self.clave=clave
        self.direccion=direccion
        self.correo=correo_electronico
        self.instancia=[]
    def append(self,nuevo):
        self.instancia.append(nuevo)
    def mostrarInstancia(self):
        Datos=[]
        for ins in self.instancia:
            Dato={
            "id": ins.getID(),
            "idConfiguracion": ins.getIDconfiguracion(),
            "nombre": ins.getNombre(),
            "fechaInicio": ins.getFechainicio(),
            "estado": ins.getEstado(),
            "fechaFinal": ins.getFechafinal()
            }
            Datos.append(Dato)
        return((Datos))


    def getNit(self):
        return self.nit
    def getNombre(self):
        return self.nombre
    def getUsuario(self):
        return self.usuario
    def getClave(self):
        return self.clave
    def getDireccion(self):
        return self.direccion
    def getCorreo(self):
        return self.correo_electronico
    
    def setNombre(self, nombre):
        self.nombre= nombre
    def setNit(self, nit):
        self.nit=nit
    def setUsuario(self, usuario):
        self.usuario=usuario
    def setClave(self, clave):
        self.clave=clave
    def setDireccion(self, direccion):
        self.direccion=direccion
    def setCorreo(self,correo_electronico):
        self.correo_electronico=correo_electronico