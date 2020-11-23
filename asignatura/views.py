from django.shortcuts import render
from django.http import HttpResponse
from asignatura.models import Asignatura

# Create your views here.
def asignaturas(request):
    Clase = Asignatura.objects.all()
    # return HttpResponse(Clase)
    return  render(request,'''''''asignatura.html',{ 'asignaturas':Clase})


def materia(request,id):
    Materia = Asignatura.objects.get(id=id)
    Estudiantes = Materia.estudiantes.all()
    # return HttpResponse(Estudiantes)
    return  render(request,'''''''asignatura_alumnos.html',{ 'materia':Materia, 'estudiantes':Estudiantes})
    # return  HttpResponse(id)