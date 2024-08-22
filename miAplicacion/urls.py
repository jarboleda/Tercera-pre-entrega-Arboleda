from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio),
    path('inicio/', views.Inicio, name='inicio'),
    path('grupos/', views.Grupos, name='grupos'),
    path('supervisores/', views.Supervisores, name='supervisores'),
    path('usuarios/', views.Usuarios, name='usuarios'),


]