from rest_framework import serializers
# from django.contrib.auth.password_validation import PasswordValidator
from .models import User, ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    
    
    

    