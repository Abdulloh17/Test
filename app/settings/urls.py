from django.urls import path
from .views import index, about, roomsdetail, reservationview

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('rooms/<int:id>', roomsdetail, name='rooms'),
    path('reservation/', reservationview, name='reservation'),

]