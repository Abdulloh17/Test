from django.contrib import admin

from todo.models import User, ToDo

# Register your models here.

admin.site.register(User)
admin.site.register(ToDo)

