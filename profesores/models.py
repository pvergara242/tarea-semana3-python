from django.db import models


# Create your models here.
class Profesor(models.Model) :
    nombre = models.CharField('Nombre Clase', max_length=80)
    direccion = models.IntegerField(blank=False, null=True)
    telefono= models.IntegerField(blank=False, null=True)



    def __str__(self) :
        return self.nombre

