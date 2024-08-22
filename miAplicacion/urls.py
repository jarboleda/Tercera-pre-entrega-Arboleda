from django.urls import path
from . import views


urlpatterns = [
    path('inicio/', views.Inicio),
    path('grupos/', views.Grupos),
    path('supervisores/', views.Supervisores),
    path('usuarios/', views.Usuarios),


]