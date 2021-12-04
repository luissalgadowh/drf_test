from django.contrib import admin
from programadores.models import Programador

# Register your models here.
@admin.register(Programador)
class ProgramadorAdmin(admin.ModelAdmin):
    model = Programador
    list_display = ('id', 'nombre', 'email', 'direccion')
    search_fields = ('id', 'nombre', 'email', 'direccion')
