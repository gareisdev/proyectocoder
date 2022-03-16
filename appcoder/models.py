from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(primary_key=True)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)
    profesion = models.CharField(max_length=60)


class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_entregado = models.DateField()
    entregado = models.BooleanField()
    calificacion_minima = models.FloatField()