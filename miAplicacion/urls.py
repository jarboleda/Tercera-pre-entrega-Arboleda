from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio),
    path('inicio/', views.Inicio, name='inicio'),
    path('gruposList/', views.gruposList, name='gruposList'),
    path('supervisoresList/', views.supervisoresList, name='supervisoresList'),
    path('usuariosList/', views.usuariosList, name='usuariosList'),
    path('gruposForm/', views.gruposForm, name='gruposForm'),
    path('supervisoresForm/', views.supervisoresForm, name='supervisoresForm'),
    path('usuariosForm/', views.usuariosForm, name='usuariosForm'),
    path('gruposBuscar/', views.gruposBuscar, name='gruposBuscar'),
    path('supervisoresBuscar/', views.supervisoresBuscar, name='supervisoresBuscar'),
    path('usuariosBuscar/', views.usuariosBuscar, name='usuariosBuscar'),
    path('buscar/', views.buscar),

    path('nuevoFormulario/', views.nuevoForm, name='nuevoFormulario'),

]