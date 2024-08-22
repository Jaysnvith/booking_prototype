from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from .models import Room, Booking
from .forms import BookingForm, RoomForm
from itertools import groupby


# HOME
def BookingHome(request):
    bookings = Booking.objects.filter(start_time__gt=timezone.now()).order_by('start_time')
    rooms = Room.objects.all().order_by('floor')  # Ensure rooms are ordered by floor
    
    # Group rooms by floor
    grouped_rooms = {floor: list(rooms) for floor, rooms in groupby(rooms, key=lambda room: room.floor)}
    
    context = {
        'bookings': bookings,
        'grouped_rooms': grouped_rooms,
    }
    
    return render(request, 'booking_app/home.html', context)

# DATA DETAIL
def RoomDetail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    bookings = room.bookings.filter(start_time__gt=timezone.now()).order_by('start_time')  # Assuming 'bookings' is the related_name in ForeignKey
    
    context = {
        'room': room,
        'bookings': bookings,
    }
    return render(request, 'booking_app/room.html', context)

class BookingDetail(DetailView):
    model = Booking
    template_name = "booking_app/booking.html"

# DATA NEW
class BookingNew(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_app/update.html"
    success_url = reverse_lazy("booking_app:home")

# DATA UPDATE
class BookingUpdate(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_app/update.html"
    def get_success_url(self):
        return reverse('booking_app:booking', kwargs={'pk': self.object.pk})

class RoomUpdate(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = "booking_app/update.html"
    success_url = reverse_lazy("booking_app:home")
    def get_success_url(self):
        return reverse('booking_app:room', kwargs={'pk': self.object.pk})

# DATA DELETE
class RoomDelete(DeleteView):
    model = Room
    template_name = "booking_app/delete.html"

class BookingDelete(DeleteView):
    model = Booking
    template_name = "booking_app/delete.html"