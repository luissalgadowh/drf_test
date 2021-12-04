from django.core.cache import cache
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from programadores.models import Programador
from programadores.views_api.serializers import ProgramadorSerializer

# from rest_framework.permissions import IsAuthenticated


class ViewsetProgramador(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer

class ProgramadorApi(generics.ListAPIView):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer

class ProgramadorCreateApi(generics.CreateAPIView):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer

class ProgramadorUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer

class ProgramadorDeleteApi(generics.DestroyAPIView):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer