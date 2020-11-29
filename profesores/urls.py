from django.urls import path
from profesores.views import profesores,profesor

app_name = 'estudiantes/'
urlpatterns = [
    path('', profesores),
    path('<profesor_id>',profesor),
]