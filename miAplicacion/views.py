from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from datetime import date
from miAplicacion.models import Grupos, Supervisores, Usuarios
from miAplicacion.forms import nuevoFormulario

# Create your views here.

def Inicio(req):
# Vista de inicio

    return render(req, "miaplicacion/index.html")


def gruposList(req):
# Vista para listar los grupos ingresados

    gruposTodos = Grupos.objects.all()
    return render(req, "miaplicacion/grupos.html", {'gruposTodos': gruposTodos})


def supervisoresList(req):
# Vista para listar los supervisores ingresados

    supervisoresTodos = Supervisores.objects.all()
    return render(req, "miaplicacion/supervisores.html", {'supervisoresTodos': supervisoresTodos})


def usuariosList(req):
# Vista para listar los usuarios ingresados

    usuariosTodos = Usuarios.objects.all()
    return render(req, "miaplicacion/usuarios.html", {'usuariosTodos': usuariosTodos})


def gruposForm(req):
# Vista del formulario para agregar nuevos grupos

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Grupos(codigo=cod, nombre=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('gruposList')

    return render(req, 'miaplicacion/gruposForm.html')


def supervisoresForm(req):
# Vista del formulario para agregar nuevos supervisores

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Supervisores(codigo=cod, nombres=req.POST['nombre'], idioma=req.POST['idioma'], email=req.POST['email'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('supervisoresList')
    
    return render(req, 'miaplicacion/supervisoresForm.html')


def usuariosForm(req):
# Vista del formulario para agregar nuevos usuarios

    if req.method == 'POST':
        cod = str(random.randint(10000,99999))
        sta = "A"
        cre = date.today()
        grupo = Usuarios(codigo=cod, nombres=req.POST['nombre'], idioma=req.POST['idioma'], estado=sta, creacion=cre)
        grupo.save()

        return redirect('usuariosList')
    
    return render(req, 'miaplicacion/usuariosForm.html')


def buscar(req):
# Vista del formulario para buscar
    
    if req.GET['codigo']:
        cod = req.GET['codigo']
        tipo = req.GET['tipo']

        if tipo == '1':
            obj = Grupos
        elif tipo == '2':
            obj = Supervisores
        else:
            obj = Usuarios

        datos = obj.objects.filter(codigo__icontains=cod)

        return render(req, 'miaplicacion/resultados.html', {'datos': datos, 'codigo': cod, 'tipo': tipo})
  
    else:
        return render(req, 'miaplicacion/index.html')


def nuevoForm(req):

    if req.method == 'POST':

        miFormulario = nuevoFormulario(req.POST)
        # print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            cod = str(random.randint(10000,99999))
            sta = "A"
            cre = date.today()

            grupo = Usuarios(codigo=cod, nombres=informacion['nombre'], idioma=informacion['idioma'], estado=sta, creacion=cre)
            grupo.save()

            return render(req, 'miaplicacion/index.html')
        
    else:
        miFormulario = nuevoFormulario()

    return render(req, 'miaplicacion/nuevoFormulario.html', {"miFormulario": miFormulario})
