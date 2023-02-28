from django.contrib import admin

from todo.models import ToDo
from users.models import User

# Register your models here.

admin.site.register(User)
admin.site.register(ToDo)

