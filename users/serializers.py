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


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255, write_only=True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only=True
    )
    class Meta:
        model = User 
        fields = ('username', 'email', 'phone_number', 'age', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email = self.initial_data.get("email"),
            phone_number = self.initial_data.get("phone_number"),
            age = self.initial_data.get("age"),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


