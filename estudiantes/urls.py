from django.urls import path
from estudiantes.views import  estudiantes,estudiante

urlpatterns = [
    path('', estudiantes),
    path('estudiante/<id>/', estudiante),
]