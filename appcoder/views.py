from dataclasses import fields
from datetime import datetime
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from appcoder.models import Curso, Entregable, Estudiante, Profesor, Avatar
from appcoder.forms import CursoFormulario, UsuarioRegistroForm, UsuarioEditForm, AvatarFormulario


# Vistas basadas en clases

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Autenticacion Django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:
        imagen = avatar[0].imagen.url


    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    return render(request, "appcoder/index.html", dict_ctx)

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "appcoder/estudiantes.html", {"estudiantes": estudiantes, "title": "Estudiantes", "page": "Estudiantes"})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appcoder/profesores.html", {"profesores": profesores, "title": "Profesores", "page": "Profesores"})

def cursos(request):
    print(request)

    cursos = Curso.objects.all()

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso = Curso(data['nombre'], data['camada'])
            curso.save()

            return redirect('Inicio')
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


class CursoLista(LoginRequiredMixin, ListView):

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


def login_request(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)
                
                dict_ctx = {"title": "Inicio", "page": usuario }
                return render(request, "appcoder/index.html", dict_ctx)
            else:
                dict_ctx = {"title": "Inicio", "page": usuario, "errors": ["El usuario no existe"] }
                return render(request, "appcoder/index.html", dict_ctx)
        else:
            dict_ctx = {"title": "Inicio", "page": "anonymous", "errors": ["Revise los datos indicados en el form"] }
            return render(request, "appcoder/index.html", dict_ctx)
    else:
        form = AuthenticationForm()
        return render(request, "appcoder/login.html", {"form": form})


def register_request(request):

    if request.method == "POST":

        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            print(usuario)
            form.save()
            return redirect("Inicio")
        else:
            dict_ctx = {"title": "Inicio", "page": "anonymous", "errors": ["No paso las validaciones"] }
            return redirect(request, "appcoder/index.html", dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request, "appcoder/register.html", {"form": form})


@login_required()
def actualizar_usuario(request):
    
    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]

            usuario.save()

            return redirect("Inicio")
        else:
            formulario = UsuarioEditForm(initial={"email": usuario.email})  
            return render(request,  "appcoder/editar_usuario.html", {"form": formulario, "errors": ["Datos invalidos"]})

    else:
        formulario = UsuarioEditForm(initial={"email": usuario.email})  
        return render(request,  "appcoder/editar_usuario.html", {"form": formulario})


@login_required()
def cargar_imagen(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("Inicio")
    else:

        formulario = AvatarFormulario()
        return render(request, "appcoder/cargar_imagen.html", {"form": formulario})
