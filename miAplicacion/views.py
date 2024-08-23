from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from datetime import date
from miAplicacion.models import Grupos, Supervisores, Usuarios

# Create your views here.

def Inicio(req):
    return render(req, "miaplicacion/index.html")

def gruposList(req):
    gruposTodos = Grupos.objects.all()
    return render(req, "miaplicacion/grupos.html",{'gruposTodos': gruposTodos})

def supervisoresList(req):
    return render(req, "miaplicacion/supervisores.html")

def usuariosList(req):
    return render(req, "miaplicacion/usuarios.html")

def gruposForm(req):

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        grupo = Grupos(codigo=cod, nombre=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=date.today())
        grupo.save()

        return redirect('gruposList')

    return render(req, 'miaplicacion/gruposForm.html')

def supervisoresForm(req):
    return render(req, 'miaplicacion/supervisoresForm.html')

def usuariosForm(req):
    return render(req, 'miaplicacion/usuariosForm.html')
