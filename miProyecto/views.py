from django.http import HttpResponse
from datetime import date, datetime
from django.template import Template, Context
from django.template import loader

from miAplicacion.models import Grupos, Supervisores, Usuarios
import random

""" 
def saludo(req):
    return HttpResponse("Hola Django - Coder")

def dia_hoy(req):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")

def nombre(req, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

def plantilla(req):
    miHtml = open('miProyecto/plantillas/plantilla1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def plantilla2(req):
    nom = 'Javier'
    ape = 'Arboleda'

    diccionario = {"nombre": nom, "apellido": ape, "hoy": datetime.now()}

    miHtml = open('miProyecto/plantillas/plantilla1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def plantilla3(req):

    nom = 'Javier'
    ape = 'Arboleda'

    listadenotas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    diccionario = {"nombre": nom, "apellido": ape, "hoy": datetime.now(), "notas": listadenotas}

    miHtml = open('miProyecto/plantillas/plantilla1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def plantilla4(req):

    nom = 'Javier'
    ape = 'Arboleda'

    listadenotas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    diccionario = {"nombre": nom, "apellido": ape, "hoy": datetime.now(), "notas": listadenotas}
    
    plantilla = loader.get_template('plantilla1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) 

"""

def agregaGrupo(req, nom, idi):

    cod = str(random.randint(10000,99999))
    sta = "A"
    grupo = Grupos(codigo=cod, nombre=nom, idioma=idi, estado=sta, creacion=date.today())
    grupo.save()

    return HttpResponse("Se agregó el grupo")
