from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import date

# Create your views here.

def Inicio(req):
    return render(req, "miaplicacion/index.html")

def Grupos(req):
    return render(req, "miaplicacion/grupos.html")

def Supervisores(req):
    return render(req, "miaplicacion/supervisores.html")

def Usuarios(req):
    return render(req, "miaplicacion/usuarios.html")


def agregaGrupo(req, nom, idi):

    cod = str(random.randint(10000,99999))
    sta = "A"
    grupo = Grupos(codigo=cod, nombre=nom, idioma=idi, estado=sta, creacion=date.today())
    grupo.save()

    return HttpResponse("Se agregó el grupo")
