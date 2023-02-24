from django.shortcuts import render

from .models import Settings, About, Rooms, Reservation
# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    rooms = Rooms.objects.all()

    context = {
        'setting': setting,
        'rooms': rooms,

    }

    return render(request, '02_index.html', context)


def about(request):
    setting = Settings.objects.latest('id')
    about = About.objects.latest('id')
    context = {
        'setting': setting,
        'about':about
    }

    return render(request, 'about.html', context)


def roomsdetail(request, id):
    rooms = Rooms.objects.get(id = id)
    setting = Settings.objects.latest('id')

    context = {
        'rooms': rooms,
        'setting': setting,

    }

    return render(request, 'hotel_details.html', context)


def reservationview(request):
    reservation = Reservation.objects.all()
    rooms = Rooms.objects.all()
    setting = Settings.objects.latest('id')

    context = {
        'rooms': rooms,
        'setting': setting,
        'reservation': reservation,
        

    }

    return render(request, 'checkout.html', context)