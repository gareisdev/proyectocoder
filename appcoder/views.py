from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Estudiante


# Create your views here.

def inicio(request):
    date_init = datetime.now()
    dict_ctx = {"title": "Inicio", "message": "Bienvenid@"}
    return render(request, "appcoder/index.html", dict_ctx)

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def cursos(request):
    return HttpResponse("vista de cursos")

def entregables(request):
    return HttpResponse("vista de entregables")
