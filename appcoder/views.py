from dataclasses import fields
from datetime import datetime
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render

from appcoder.models import Curso, Entregable, Estudiante, Profesor
from appcoder.forms import CursoFormulario


# Vistas basadas en clases

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso = Curso(data['nombre'], data['camada'])
            curso.save()

            formulario = CursoFormulario()
            return render(request, "appcoder/cursos.html", {"cursos": cursos, "title": "Cursos", "page": "Cursos", "formulario": formulario})
    else:   
        
        formulario = CursoFormulario()
        return render(request, "appcoder/cursos.html", {"cursos": cursos, "title": "Cursos", "page": "Cursos", "formulario": formulario})

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "appcoder/entregables.html", {"entregables":entregables,"title": "Entregables", "page": "Entregables"})

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


def borrar_curso(request, camada_id):
    try:
        curso = Curso.objects.get(camada=camada_id)
        curso.delete()

        return render(request, "appcoder/index.html")
    except Exception as exc:
        return render(request, "appcoder/index.html")


def actualizar_curso(request, camada_id):

    curso = Curso.objects.get(camada=camada_id)


    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():

            informacion = formulario.cleaned_data


            curso.nombre = informacion["nombre"]
            
            curso.save()

            return render(request, "appcoder/index.html")

    else:

        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})

        return render(request, "appcoder/update_curso.html", {"formulario": formulario, "camada_id":camada_id})


class CursoLista(ListView):

    model = Curso
    template_name = "appcoder/cursos_list.html"

class CursoDetalle(DetailView):

    model = Curso
    template_name = "appcoder/curso_detalle.html"

class CursoCrear(CreateView):

    model = Curso
    success_url = "/appcoder/curso/list"
    fields = ['nombre', 'camada']

class CursoActualizar(UpdateView):

    model = Curso
    success_url = "/appcoder/curso/list"
    fields = ['nombre']


class CursoBorrar(DeleteView):

    model = Curso
    success_url = "/appcoder/curso/list"