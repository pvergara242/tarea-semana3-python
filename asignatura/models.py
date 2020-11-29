from django.db import models
from profesores.models import Profesor


# Create your models here.
class Asignatura(models.Model) :
    name = models.CharField('Nombre Clase', max_length=80)
    aforo = models.IntegerField(blank=False, null=True)
    duration = models.IntegerField(blank=False, null=True)
    estado = models.BooleanField('Activo/Inactivo', default=False)

    profesores = models.ManyToManyField(Profesor, related_name='asignaturas')
    class Meta :
        ordering = ['name']
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self) :
        return self.name
