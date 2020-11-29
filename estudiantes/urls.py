from django.urls import path
from estudiantes.views import estudiantes,estudiante

app_name = 'estudiantes/'
urlpatterns = [
    path('', estudiantes),
    path('<estudiante_id>',estudiante),
    # path('delete/<int:estudiante_id>', views.delete),
    # path('estudiante/<id>/', estudiante),
]