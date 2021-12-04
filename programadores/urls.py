from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from programadores.views.home import lista_programadores, crear_programador, editar_programador

urlpatterns = [
    path('', lista_programadores, name="lista_programadores"),
    path('programador/crear/', crear_programador, name="crear_programador"),
    path('programador/editar/<int:pk>/', editar_programador, name="editar_programador"),
]