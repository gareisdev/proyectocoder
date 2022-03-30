from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(primary_key=True)


    def __str__(self):
        return f"{self.nombre} | {self.camada}"

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)
    profesion = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_entregado = models.DateField()
    entregado = models.BooleanField()
    calificacion_minima = models.FloatField()

    def __str__(self) -> str:
        return f"{self.nombre} - {self.fecha_entregado}"