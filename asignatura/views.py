from django.shortcuts import render,redirect
from django.http import HttpResponse
from asignatura.models import Asignatura
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from asignatura.serializadores import AsignaturaSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def asignaturas(req):
    if req.method=='GET':
        asignaturas = Asignatura.objects.all()
        serialized = AsignaturaSerializer(asignaturas, many=True)
        return Response(status=status.HTTP_200_OK, data = serialized.data)
    if req.method=='POST':
        asignaturas = AsignaturaSerializer(data=req.data)
        if asignaturas.is_valid():
            asignaturas.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)

@api_view(['PUT','DELETE','GET'])
def asignatura(req,asignatura_id) :
        asignatura = Asignatura.objects.get(id=asignatura_id)
        if req.method == 'GET':
            serialized = AsignaturaSerializer(asignatura)
            return Response(status=status.HTTP_200_OK,data = serialized.data)
        if req.method=='PUT':
            serialized = AsignaturaSerializer(instance = asignatura , data = req.data, partial = True)
            if serialized.is_valid():
                    serialized.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
        if req.method == 'DELETE':
            asignatura.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)









