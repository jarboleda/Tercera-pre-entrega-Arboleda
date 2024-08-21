from django.http import HttpResponse
from datetime import date
from django.template import Template, Context

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