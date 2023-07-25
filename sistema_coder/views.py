from django.http import HttpResponse

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar_con_fecha(request):
    hoy = datetime.now
    saludar_con_fecha =  f"hola querido usuario: hoy es{hoy}"
    
    respuesta_http = HttpResponse(saludar_con_fecha)
    return respuesta_http



def inicio(request):
    
    
    http_response = render (
        request=request,
        template_name="inicio.html",
        context = {
                    }    
    )
    return http_response

