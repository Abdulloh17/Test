from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Название сайта',
    )
    descriptions = models.TextField(
        verbose_name='Описание сайта',
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип сайта',
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Телефонный номер',
        blank=True, null=True,
    )
    email = models.EmailField(
        verbose_name='Ваша почта',
        blank=True, null=True,
    )
    address = models.CharField(
        max_length=255,
        verbose_name= 'Ваш адрес',
        blank=True, null=True,
    )
    instagram = models.URLField(
        verbose_name='Ваш инстаграм',
    )
    facebook = models.URLField(
        verbose_name='Ваш фейсбук',
    )
    youtube = models.URLField(
        verbose_name='Ваш ютуб',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class About(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="О нас"
    )


class Rooms(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название комнаты',
    )
    roomimage = models.ImageField(
        upload_to='roomimgs/',
        verbose_name='Фото комнат',
    )
    description = models.TextField(
        verbose_name='Описание комнаты',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена за день'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Reservation(models.Model):
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE,
        verbose_name='Выберите комнату',
        
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Ваше имя',
    )
    lastname = models.CharField(
        max_length=255,
        verbose_name='Ваша фамилия'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Ваш номер',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'