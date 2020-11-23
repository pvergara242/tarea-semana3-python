from django.shortcuts import render
from django.http import HttpResponse
from estudiantes.models import Estudiante

# Create your views here.
def estudiantes(request):
    Elemento = Estudiante.objects.all()
    return  render(request,'''''''lista_estudiantes.html',{ 'estudiantes':Elemento})

def estudiante(request,id):
    Elemento = Estudiante.objects.get(id=id)
    Materias = Elemento.asignatura.all()
    return  render(request,'''''''estudiante.html',{ 'estudiante':Elemento, 'Materia':Materias})
    # return  HttpResponse(id)
