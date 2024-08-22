from django.db import models
from django.utils import timezone
from datetime import timedelta

class Room(models.Model):
    class FloorChoices(models.IntegerChoices):
        FIRST = 1, '1st Floor'
        SECOND = 2, '2nd Floor'
        THIRD = 3, '3rd Floor'
        
    class UsageChoices(models.IntegerChoices):
        UNAVAILABLE = 1, 'Unavailable'
        AVAILABLE = 0, 'Available'
    
    name = models.CharField(max_length=50, verbose_name="Room Name")
    capacity = models.PositiveIntegerField(verbose_name="Capacity")
    floor = models.IntegerField(choices=FloorChoices.choices, verbose_name="Floor")
    facility = models.TextField(blank=True, null=True, verbose_name="Facilities")
    status = models.IntegerField(choices=UsageChoices.choices, verbose_name="Status")

    def __str__(self):
        return self.name

class Booking(models.Model):
    class UsageChoices(models.TextChoices):
        INTERNAL = 'i', 'Internal'
        EXTERNAL = 'e', 'External'
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings", verbose_name="Room")
    start_time = models.DateTimeField(verbose_name="Start Time", default=(timezone.now()+timedelta(hours=1)))
    end_time = models.DateTimeField(verbose_name="End Time", default=(timezone.now()+timedelta(hours=2)))
    usage = models.CharField(max_length=1, choices=UsageChoices.choices, verbose_name="Usage")
    request = models.TextField(blank=True, null=True, verbose_name="Special Requests")

    def __str__(self):
        return f"{self.room.name} - {self.start_time} - {self.end_time}"
