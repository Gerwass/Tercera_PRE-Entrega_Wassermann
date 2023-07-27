from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from control_estudios.forms import CursoFormulario,EstudianteFormulario, ProfesorFormulario


from control_estudios.models import Curso, Estudiante, Profesor


# Create your views here.
def listar_estudiantes(request):
    contexto = {
        
        "estudiantes": Estudiante.objects.all()
    }
    http_response = render(
    request=request,
    template_name='control_estudios/lista_estudiante.html',
    context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto =  {
            
        "cursos":Curso.objects.all()
    }


    http_response = render(
    request=request,
    template_name='control_estudios/lista_cursos.html',
    context=contexto,
    )
    return http_response

def listar_profesores(request):
    contexto = {
        
        "profesores": Profesor.objects.all()
    }
    http_response = render(
    request=request,
    template_name='control_estudios/lista_profesores.html',
    context=contexto,
    )
    return http_response


def crear_estudiante(request):
   if request.method == "POST":
       formulario = EstudianteFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           apellido = data["apellido"]
           email = data["email"]
           dni = data["dni"]
           
           estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email, dni=dni)  # lo crean solo en RAM
           estudiante.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_estudiante')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
        formulario = EstudianteFormulario()
        http_response = render(
       request=request,
       template_name='control_estudios/formulario_estudiante.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_estudiante(request):
    if request.method == "POST":
       data = request.POST
       busqueda = data.get("busqueda")
       estudiante = Estudiante.objects.filter(apellido__contains=busqueda)
    else: 
       estudiante = []
    contexto = {
           "estudiante": estudiante,
       }
    http_response = render(
    request=request,
    template_name='control_estudios/lista_estudiante.html',
    context=contexto,
       )
    return http_response




def crear_cursos(request):
   if request.method == "POST":
       formulario = CursoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           comision = data["comision"]
           curso = Curso(nombre=nombre, comision=comision)  # lo crean solo en RAM
           curso.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_cursos')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
        formulario = CursoFormulario()
        http_response = render(
       request=request,
       template_name='control_estudios/formulario_curso.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_cursos(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       cursos = Curso.objects.filter(comision__contains=busqueda)
       contexto = {
           "cursos": cursos,
       }
       http_response = render(
           request=request,
           template_name='control_estudios/lista_cursos.html',
           context=contexto,
       )
       return http_response
   
def crear_profesor(request):
   if request.method == "POST":
       formulario = ProfesorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           apellido = data["apellido"]
           email = data["email"]
           dni = data["dni"]
           
           profesor = Profesor(nombre=nombre, apellido=apellido, email=email, dni=dni)  # lo crean solo en RAM
           Profesor.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_profesores')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
        formulario = ProfesorFormulario()
        http_response = render(
       request=request,
       template_name='control_estudios/formulario_profesor.html',
       context={'formulario': formulario}
   )
   return http_response