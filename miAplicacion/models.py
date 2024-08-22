from django.db import models

# Create your models here.

class Grupos(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    idioma = models.CharField(max_length=20)
    estado = models.CharField(max_length=1)
    creacion = models.DateField()

    def __str__(self):
        return f"Código: {self.codigo} - Nombre: {self.nombre} - Idioma: {self.idioma} - Estado: {self.estado} - Creado: {self.creacion}"

class Supervisores(models.Model):
    codigo = models.IntegerField()
    nombres = models.CharField(max_length=50)
    idioma = models.CharField(max_length=20)
    email = models.EmailField()
    grupo = models.IntegerField()
    estado = models.CharField(max_length=1)
    creacion = models.DateField()

    def __str__(self):
        return f"Código: {self.codigo} - Nombres: {self.nombres} - Idioma: {self.idioma} - Email: {self.email} - Grupo: {self.grupo} - Estado: {self.estado} - Creado: {self.creacion}"

class Usuarios(models.Model):
    codigo = models.IntegerField()
    nombres = models.CharField(max_length=50)
    idioma = models.CharField(max_length=20)
    grupo = models.IntegerField()
    estado = models.CharField(max_length=1)
    creacion = models.DateField()

    def __str__(self):
        return f"Código: {self.codigo} - Nombres: {self.nombres} - Idioma: {self.idioma} - Grupo: {self.grupo} - Estado: {self.estado} - Creado: {self.creacion}"

