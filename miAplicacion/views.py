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
    return render(req, "miaplicacion/grupos.html", {'gruposTodos': gruposTodos})

def supervisoresList(req):
    supervisoresTodos = Supervisores.objects.all()
    return render(req, "miaplicacion/supervisores.html", {'supervisoresTodos': supervisoresTodos})

def usuariosList(req):
    usuariosTodos = Usuarios.objects.all()
    return render(req, "miaplicacion/usuarios.html", {'usuariosTodos': usuariosTodos})

def gruposForm(req):

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Grupos(codigo=cod, nombre=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('gruposList')

    return render(req, 'miaplicacion/gruposForm.html')

def supervisoresForm(req):

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Supervisores(codigo=cod, nombres=req.POST['nombre'], idioma=req.POST['idioma'], email=req.POST['email'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('supervisoresList')
    
    return render(req, 'miaplicacion/supervisoresForm.html')

def usuariosForm(req):

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Usuarios(codigo=cod, nombres=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('usuariosList')
    
    return render(req, 'miaplicacion/usuariosForm.html')
