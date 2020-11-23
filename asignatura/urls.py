from django.urls import path
from asignatura.views import  asignaturas,materia

urlpatterns = [
    path('', asignaturas),
    path('materias/<id>/', materia),
]