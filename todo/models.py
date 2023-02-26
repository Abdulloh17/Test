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
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        verbose_name='Эл. почта'
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


class ToDo(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Названия задания'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус задания'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    image = models.ImageField(
        verbose_name='Добавление фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    
    