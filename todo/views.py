from django.shortcuts import render
from rest_framework import generics

from .models import User, ToDo
from .serializers import UserSerializer, ToDoSerializer

# Create your views here.
class TodoCreateApi(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class UserCreateApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

