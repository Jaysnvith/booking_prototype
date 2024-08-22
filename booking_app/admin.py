from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'floor', 'facility','status')
    list_filter = ('floor','status')
    search_fields = ('name', 'facility')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time', 'usage', 'request')
    list_filter = ('room', 'start_time', 'usage')
    search_fields = ('room__name', 'request')
