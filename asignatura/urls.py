from django.urls import path
from asignatura.views import asignaturas,asignatura

app_name = 'estudiantes/'
urlpatterns = [
    path('', asignaturas),
    path('<asignatura_id>',asignatura),
    # path('delete/<int:estudiante_id>', views.delete),
    # path('estudiante/<id>/', estudiante),
]