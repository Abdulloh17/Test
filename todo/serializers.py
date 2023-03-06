from rest_framework import serializers
# from django.contrib.auth.password_validation import PasswordValidator
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user', 'title', 'description', 'is_completed', 'created_at', 'image')






    
    
    

    