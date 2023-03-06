# Generated by Django 4.1.7 on 2023-03-06 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Эл. почта')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+996...'.", regex='^\\+996\\d{9}$')], verbose_name='Тел. номер')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('age', models.IntegerField(verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователь',
            },
        ),
    ]
