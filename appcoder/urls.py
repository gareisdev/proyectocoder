from unicodedata import name
from django.urls import path
from appcoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('estudiantes/', estudiantes, name="Estudiantes"),    
    path('profesores/', profesores, name="Profesores"),    
    path('cursos/', cursos, name="Cursos"),    
    path('entregables/', entregables, name="Entregables")
]
