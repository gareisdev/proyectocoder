
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):

    # Campos del formulario
    nombre = forms.CharField(max_length=40) # Campo con restricciones
    camada = forms.IntegerField()



class UsuarioRegistroForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { k: "" for k in fields}


class UsuarioEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'password2']
        help_text = { k: "" for k in fields}


class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()