from django.shortcuts import render

# Create your views here.


from appcoder.models import Curso

curso = Curso.objects.get(camada=26370)
curso.delete()