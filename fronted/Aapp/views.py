from email.policy import HTTP
from django.http import HttpResponse
import string
from urllib import response
from xmlrpc.client import ResponseError

from django.shortcuts import render


#from Aapp.forms import FileForm, DateForm, DateForm2
#from frontend.settings import PDF_FILES_FOLDER
from django.http import FileResponse
# Create your views here.


#endpoint = 'http://127.0.0.1:4000/'
def index(requests):
    return render(requests, 'index.html',{})
def CargaMasiva(requests):
    return render(requests, 'carga.html',{})
def Operaciones(requests):
    return render(requests, 'operaciones.html',{})
def Creacion(requests):
    return render(requests, 'creacion.html',{})
def Consultar(requests):
    return render(requests, 'consultar.html',{})
def ejemplo(requests):
    return HttpResponse("prueba")