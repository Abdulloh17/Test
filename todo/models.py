from django.db import models


# Create your models here.


class ToDo(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Названия задания',
        unique=True,
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
    
    