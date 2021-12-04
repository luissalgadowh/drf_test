from rest_framework import serializers

from programadores.models import Programador

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        fields = ['id', 'nombre', 'email', 'direccion']
