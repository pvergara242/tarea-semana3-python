from django.shortcuts import render,redirect
from django.http import HttpResponse
from estudiantes.models import Estudiante
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from estudiantes.serializadores import EstudianteSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def estudiantes(req):
    if req.method=='GET':
        estudiantes = Estudiante.objects.all()
        serialized = EstudianteSerializer(estudiantes, many=True)
        return Response(status=status.HTTP_200_OK, data = serialized.data)
    if req.method=='POST':
        estudiantes = EstudianteSerializer(data=req.data)
        if estudiantes.is_valid():
            estudiantes.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)

@api_view(['PUT','DELETE','GET'])
def estudiante(req,estudiante_id) :
        estudiante = Estudiante.objects.get(id=estudiante_id)
        if req.method == 'GET':
            serialized = EstudianteSerializer(estudiante)
            return Response(status=status.HTTP_200_OK,data = serialized.data)
        if req.method=='PUT':
            serialized = EstudianteSerializer(instance = estudiante , data = req.data, partial = True)
            if serialized.is_valid():
                    serialized.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
        if req.method == 'DELETE':
            estudiante.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)









# class  Estudiantes(View):
#     http_method_names = ['get','post']
#     def  get(self,request):
#             elemento = Estudiante.objects.all()
#             return  render(request,'lista_estudiantes.html',{ 'estudiantes':elemento})
#
#     def post(self, request) :
#         estudiantes_data= {
#             'nombre': request.POST['nombre'],
#             'direccion': request.POST['direccion'],
#             'telefono':request.POST['telefono']
#         }
#         elemento = Estudiante.objects.create(**estudiantes_data)
#         return  redirect('estudiantes/:view')
#
#     def put(self, request, estudiantes_data) :
#         estudiante_data={
#             'nombre': request.PUT['nombre'],
#             'direccion': request.PUT['direccion'],
#             'telefono': request.PUT['telefono']
#         }
#         elemento = Estudiante.objects.update(**estudiantes_data)
#         return redirect('estudiantes/:view')
#
# def estudiante(request,id):
#         Elemento = Estudiante.objects.get(id=id)
#         Materias = Elemento.asignatura.all()
#         return  render(request,'estudiante.html',{ 'estudiante':Elemento, 'Materia':Materias})
#         # return  HttpResponse(id)
