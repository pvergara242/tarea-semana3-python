from rest_framework import serializers
from asignatura.models import Asignatura

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asignatura
        fields=('name', 'aforo', 'duration','estado')