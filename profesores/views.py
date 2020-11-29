from django.shortcuts import render,redirect
from django.http import HttpResponse
from profesores.models import Profesor
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from profesores.serializadores import ProfesorSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def profesores(req):
    if req.method=='GET':
        profesores = Profesor.objects.all()
        serialized = ProfesorSerializer(profesores, many=True)
        return Response(status=status.HTTP_200_OK, data = serialized.data)
    if req.method=='POST':
        profesores = ProfesorSerializer(data=req.data)
        if profesores.is_valid():
            profesores.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)

@api_view(['PUT','DELETE','GET'])
def profesor(req,profesor_id) :
        profesor= Profesor.objects.get(id=profesor_id)
        if req.method == 'GET':
            serialized = ProfesorSerializer(profesor)
            return Response(status=status.HTTP_200_OK,data = serialized.data)
        if req.method=='PUT':
            serialized = ProfesorSerializer(instance = profesor , data = req.data, partial = True)
            if serialized.is_valid():
                    serialized.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
        if req.method == 'DELETE':
            profesor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)









