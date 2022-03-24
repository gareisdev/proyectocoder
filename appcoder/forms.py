
from django import forms

class CursoFormulario(forms.Form):

    # Campos del formulario
    nombre = forms.CharField(max_length=40) # Campo con restricciones
    camada = forms.IntegerField()