from django.db import models


# Create your models here.
class Asignatura(models.Model) :
    name = models.CharField('Nombre Clase', max_length=80)
    aforo = models.IntegerField(blank=False, null=True)
    duration = models.IntegerField(blank=False, null=True)
    estado = models.BooleanField('Activo/Inactivo', default=False)


    class Meta :
        ordering = ['name']
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self) :
        return self.name
