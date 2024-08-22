"""
URL configuration for miProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miProyecto import views #saludo, dia_hoy, nombre, plantilla, plantilla2, plantilla3, plantilla4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo),
    path('dia_hoy/', views.dia_hoy),
    path('nombre/<nombre>', views.nombre),
    path('plantilla/', views.plantilla),
    path('plantilla2/', views.plantilla2),
    path('plantilla3/', views.plantilla3),
    path('plantilla4/', views.plantilla4),
]


