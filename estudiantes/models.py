from django.db import models
from asignatura.models import Asignatura

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)

    asignatura = models.ManyToManyField(Asignatura,related_name="estudiantes")



    def  __str__(self) :
            return self.nombre

