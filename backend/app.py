from flask import Flask, request,app
from flask.json import jsonify
from flask_cors import CORS
from configuracion import configuracion
from instancia import instancia
from cliente import cliente
from recurso import recurso
from categoria import categoria
app = Flask(__name__)
CORS(app)
clientes=[]
categorias=[]
instancias=[]
recursos=[]




@app.route('/')
def home():
    return "Esto funciona :D"
@app.route('/consultarDatos',methods=['GET'])
def consultarDatos():
    global clientes
    Datos=[]
    for cliente in clientes:
        Dato={
            "nit": cliente.getNit(),
            "nombre": cliente.getNombre(),
            "usuario": cliente.getUsuario(),
            "clave": cliente.getClave(),
            "direccion": cliente.getDireccion(),
            "instancias":cliente.mostrarInstancia()
        }
        Datos.append(Dato)
    return(jsonify(Datos))

@app.route('/crearRecurso',methods=['POST'])
def crearRecurso():
    global recursos
    recurso_repetido=False
    Nuevo_recurso=recurso(request.json["id"], request.json["nombre"],
    request.json["abreviatura"],request.json["metrica"],
    request.json["tipo"],request.json["valorXhora"])
    for recur in recursos:
        if recur.getId()==request.json["id"]:
            recurso_repetido=True
        else:
            pass
    if recurso_repetido==False:
        clientes.append(Nuevo_recurso)
        respuesta=jsonify({
           # "Error":False,
            "Mensaje":"se registro con exito"
            #,"Registro":True
        })
        return(respuesta),201
    else:
        respuesta=jsonify({
            #"error":True,
            "Mensaje":"el cliente esta repetido"
            #,"Registro":False
        })
        return(respuesta),403

@app.route('/crearCategoria',methods=['POST'])
def crearCategoria():
    global categorias
    categoria_repetida=False
    Nueva_categoria=categoria(request.json["idCategoria"], request.json["nombre"],
    request.json["descripcion"],request.json["cargaTrabajo"])
    for catego in categorias:
        if catego.getID()==request.json["idCategoria"]:
            categoria_repetida=True
        else:
            pass
        if categoria_repetida==False:
            categorias.append(Nueva_categoria)
            respuesta=jsonify({
            # "Error":False,
                "Mensaje":"se registro con exito"
                #,"Registro":True
            })
            return(respuesta),201
        else:
            respuesta=jsonify({
                #"error":True,
                "Mensaje":"la categoria esta repetido"
                #,"Registro":False
            })
            return(respuesta),403
        #  print(catego)



@app.route('/crearConfiguracion',methods=['POST'])
def crearConfiguracion():
    global categorias
    configuracion_repetida=False
    existe=False
    Nueva_configuracion=configuracion(request.json["idcategoria"],request.json["idConfiguracion"], request.json["nombre"],
    request.json["descripcion"])
    for catego in categorias:
        if catego.getID()==request.json["idCategoria"]:
            print("encontrado")
            existe=True
            catego.append(Nueva_configuracion)
            respuesta=jsonify({
                "Mensaje":"se registro con exito"
            })
            return(respuesta),201
        else:
            pass
    if existe==True:
        respuesta=jsonify({
           # "Error":False,
            "Mensaje":"se registro con exito"
            #,"Registro":True
        })
        return(respuesta),201
    else:
        respuesta=jsonify({
           # "Error":False,
            "Mensaje":"no se encontro la categoria"
            #,"Registro":True
        })
        return(respuesta),201
     
@app.route('/crearCliente',methods=['POST'])
def crearCliente():
    global clientes
    cliente_repetido=False
    Nuevo_cliente=cliente(request.json["nit"], request.json["nombre"],
    request.json["usuario"],request.json["clave"],
    request.json["direccion"],request.json["correoElectronico"])
    for client in clientes:
        if client.getNit()==request.json["nit"]:
            cliente_repetido=True
        else:
            pass
    if cliente_repetido == False:
        clientes.append(Nuevo_cliente)
        respuesta=jsonify({
           # "Error":False,
            "Mensaje":"se registro con exito"
            #,"Registro":True
        })
        return(respuesta),201
    else:
        respuesta=jsonify({
            #"error":True,
            "Mensaje":"el cliente esta repetido"
            #,"Registro":False
        })
        return(respuesta),403



@app.route('/crearInstancia',methods=['POST'])
def crearInstancia():
    global clientes
    comprobante=False
    instancia_repetida=False
    Nueva_instancia=instancia(request.json["idCliente"], request.json["id"],
    request.json["idConfiguracion"],request.json["nombre"],
    request.json["fechaInicio"],request.json["estado"],request.json["fechaFinal"])
    for client in clientes:
        if client.getNit()==request.json["idCliente"]:
            print("encontrado")
            client.append(Nueva_instancia)
            respuesta=jsonify({
                "Mensaje":"se registro con exito"
            })
            return(respuesta),201
        else:
            respuesta=jsonify({
                #"error":True,
                "Mensaje":"el cliente no ha sido encontrado"
                #,"Registro":False
            })
            return(respuesta),403
            





@app.route('/generarFactura',methods=['POST'])
def generarFactura():
    pass




if __name__ == "__main__":
    app.run( host="localhost", port = "5000", debug=True)