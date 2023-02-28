# Generated by Django 4.1.7 on 2023-02-28 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Названия задания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Статус задания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('image', models.ImageField(upload_to='', verbose_name='Добавление фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь поста')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
