from django.urls import path
from appcoder.views import *

urlpatterns = [
    path('', inicio),
    path('estudiantes/', estudiantes),    
    path('profesores/', profesores, name='Profesores'),    
    path('cursos/', cursos),    
    path('entregables/', entregables),
]
