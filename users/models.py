from django.db import models

from django.core.validators import RegexValidator
# Create your models here.

class User(models.Model):
    phone_regex = RegexValidator(
        regex= r'^\+996\d{9}$',
        message= "Номер телефона должен быть в формате: '+996...'.",
    )
    username = models.CharField(
        max_length=255,
        verbose_name='Имя пользователя',
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Эл. почта',
        unique=True,
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name='Тел. номер'
    )
    created_at = models.DateField(
        auto_now_add=True
    )
    age = models.IntegerField(
        verbose_name='Возраст'
    )

    

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'