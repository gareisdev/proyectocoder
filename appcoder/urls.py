from unicodedata import name
from django.urls import path
from appcoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="Inicio"),

    path('login/', login_request, name="Login"),
    path('register/', register_request, name="Register"),
    path('logout/', LogoutView.as_view(template_name="appcoder/logout.html"), name="Logout"),

    path('estudiantes/', estudiantes, name="Estudiantes"),    
    path('profesores/', profesores, name="Profesores"),    
    path('cursos/', cursos, name="Cursos"),    
    path('entregables/', entregables, name="Entregables"),
    path('buscarcurso/', buscar_curso, name='BuscarCurso'),
    path('borrarcurso/<camada_id>/', borrar_curso, name="eliminarCurso"),
    path('update_curso/<camada_id>/', actualizar_curso),


    path("curso/list", CursoLista.as_view(), name="curso_list"),
    path("curso/nuevo/", CursoCrear.as_view(), name="curso_create"),
    path("curso/detalle/<pk>/", CursoDetalle.as_view(), name="curso_detail"),
    path("curso/editar/<pk>/", CursoActualizar.as_view(), name="curso_update"),
    path("curso/borrar/<pk>/", CursoBorrar.as_view(), name="curso_delete")

]