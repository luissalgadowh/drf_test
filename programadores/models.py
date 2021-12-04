from django.db import models

# Create your models here.
class Programador(models.Model):

    nombre = models.CharField(max_length=80, unique=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(max_length=100, blank=True)
