from django import forms

class ProgramadorForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=80, required=True)
    email = forms.CharField(label='Correo', max_length=80, required=False)
    direccion = forms.CharField(label='Direccion', max_length=100, required=False)
