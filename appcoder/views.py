from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from appcoder.models import Curso, Entregable, Estudiante, Profesor
from appcoder.forms import CursoFormulario


# Create your views here.

def inicio(request):
    dict_ctx = {"title": "Inicio", "page": "Inicio"}
    return render(request, "appcoder/index.html", dict_ctx)

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "appcoder/estudiantes.html", {"estudiantes": estudiantes, "title": "Estudiantes", "page": "Estudiantes"})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appcoder/profesores.html", {"profesores": profesores, "title": "Profesores", "page": "Profesores"})

def cursos(request):
    cursos = Curso.objects.all()

    return render(request, "appcoder/cursos.html", {"cursos": cursos, "title": "Cursos", "page": "Cursos"})

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "appcoder/entregables.html", {"entregables":entregables,"title": "Entregables", "page": "Entregables"})

def formulario_curso(request):

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            curso = Curso(data['nombre'], data['camada'])
            curso.save()
        
        return render(request, 'appcoder/index.html')

    else:
        formulario = CursoFormulario()

        return render(request, 'appcoder/formulario_curso.html', {"formulario": formulario})

def buscar_curso(request):

    data = request.GET.get('camada', "")
    error = ""

    if data:
        try:
            curso = Curso.objects.get(camada=data)
            return render(request, 'appcoder/busqueda_curso.html', {"curso": curso, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe esa camada"
    return render(request, 'appcoder/busqueda_curso.html', {"error": error})