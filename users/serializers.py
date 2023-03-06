from rest_framework import serializers
from .models import User
from todo.serializers import ToDoSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'age')

class UsersDetailSerializer(serializers.ModelSerializer):
    users_todos = ToDoSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'age', 'users_todos')
