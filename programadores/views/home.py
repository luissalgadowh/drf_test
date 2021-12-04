import requests
import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from programadores.forms.programadores import ProgramadorForm

URL_LOCAL = "http://127.0.0.1:8000/"

def lista_programadores(request):

    url = F"{URL_LOCAL}api/programador/listar/"
    lista_programadores = []

    response = requests.get(url=url)

    if response.status_code == 200:
        content = response.content
        lista_programadores = json.loads(content)

    return render(request, 'lista_programadores.html', {'lista_programadores': lista_programadores})


def crear_programador(request):

    url = F"{URL_LOCAL}api/programador/crear/"
    form = ProgramadorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']

            headers = {
                "Content-Type": "application/json",
            }

            data = {
                'nombre': nombre,
                'email': email,
                'direccion': direccion
            }
            data = json.dumps(data)
            response = requests.post(url=url, headers=headers, data=data)
            if response.status_code == 201:
                messages.success(request, F'Se creo el programador')
                return HttpResponseRedirect(reverse('lista_programadores'))
            else:
                content = json.loads(response.content)
                print(response.content)
                messages.error(request, F'No se pudo crear al programador: {content}')

    return render(request, 'crear_programador.html', {'form': form})

def editar_programador(request, pk):

    url = F"{URL_LOCAL}api/programador/crear/"
    form = ProgramadorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']

            headers = {
                "Content-Type": "application/json",
            }

            data = {
                'nombre': nombre,
                'email': email,
                'direccion': direccion
            }
            data = json.dumps(data)
            response = requests.post(url=url, headers=headers, data=data)
            if response.status_code == 201:
                messages.success(request, F'Se creo el programador')
                return HttpResponseRedirect(reverse('lista_programadores'))
            else:
                content = json.loads(response.content)
                print(response.content)
                messages.error(request, F'No se pudo crear al programador: {content}')

    return render(request, 'editar_programador.html', {'form': form})
