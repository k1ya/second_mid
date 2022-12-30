from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.

class studentListCreate(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    
class employeeListCreate(generics.ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializer
    
class teacherListCreate(generics.ListCreateAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherSerializer

class studentUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
    
class teacherUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherSerializer
    
class employeeUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializer