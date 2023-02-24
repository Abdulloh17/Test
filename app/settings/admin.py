from django.contrib import admin

from .models import Settings, About, Rooms, Reservation
# Register your models here.
admin.site.register(Settings)
admin.site.register(About)
admin.site.register(Rooms)
admin.site.register(Reservation)



