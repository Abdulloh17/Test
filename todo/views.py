from django.shortcuts import render

from rest_framework import generics

from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TodoCreateApi(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated, )

class ToDoDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated, )




        