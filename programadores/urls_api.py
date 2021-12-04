from django.urls import include, path

from rest_framework import routers

from programadores.views_api.programadores import ProgramadorApi, ViewsetProgramador, ProgramadorCreateApi, ProgramadorUpdateApi, ProgramadorDeleteApi

router = routers.DefaultRouter()
router.register('generics', ViewsetProgramador, 'generics-olt')

urlpatterns = [
    # path('programadores/', include(router.urls)),
    path('programador/listar/', ProgramadorApi.as_view(), name='listar_programadores_api'),
    path('programador/crear/', ProgramadorCreateApi.as_view(), name="crear_programador_api"),
    path('programador/editar/<int:pk>/', ProgramadorUpdateApi.as_view(), name="editar_programador_api"),
    path('programador/eliminar/<int:pk>/', ProgramadorDeleteApi.as_view(), name="eliminar_programador_api"),
]

