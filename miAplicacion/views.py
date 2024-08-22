from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def Inicio(req):
    return render(req, "miaplicacion/index.html")

def Grupos(req):
    return render(req, "miaplicacion/grupos.html")

def Supervisores(req):
    return render(req, "miaplicacion/supervisores.html")

def Usuarios(req):
    return render(req, "miaplicacion/usuarios.html")

