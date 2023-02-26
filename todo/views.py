from django.shortcuts import render
from rest_framework import generics

from .models import User, ToDo
from .serializers import UserSerializer, ToDoRegisterSerializer, ToDoSerializer, UserRegisterSerializer

# Create your views here.

class ToDoListApi(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class TodoCreateApi(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoRegisterSerializer

class UserListApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

class UserRegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

