from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    phone_regex = RegexValidator(
        regex= r'^\+996\d{9}$',
        message= "Номер телефона должен быть в формате: '+996...'.",
    )
    email = models.EmailField(
        verbose_name="Ваша почта",
        unique=True
        )
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Ваш тел.номер"
    )
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    age = models.CharField(
        max_length=255,
        verbose_name="Ваш возраст"
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"