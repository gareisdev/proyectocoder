from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inicio(request):
    dict_ctx = {"title": "Inicio", "message": "Bienvenid@"}
    return render(request, "appcoder/index.html", dict_ctx)

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")