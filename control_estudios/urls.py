"""
URL configuration for sistema_coder project.

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

from control_estudios.views import (listar_estudiantes,listar_cursos,crear_cursos, buscar_cursos,crear_estudiante,listar_profesores,
                                    buscar_estudiante,crear_profesor, buscar_profesor)
#URLS ESPECIFICAS DE LA APP

urlpatterns = [
    path("estudiantes/",listar_estudiantes, name ="lista_estudiante"),
    path("cursos/",listar_cursos, name ="lista_cursos"),
    path("crear-curso/", crear_cursos, name = "crear_cursos"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("eprofesores/",listar_profesores, name ="lista_profesores"),
    path("registro-estudiante/",crear_estudiante, name = "crear_estudiante"),
    path("buscar-estudiante/",buscar_estudiante, name = "buscar_estudiante"),
    path("crear-profesores/",crear_profesor, name = "crear_profesores"),
    path("buscar-profesor/",buscar_profesor, name = "buscar_profesor"),
]