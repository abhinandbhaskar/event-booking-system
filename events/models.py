from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Events(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=200)
    total_seats=models.PositiveIntegerField()
    booked_seats=models.PositiveIntegerField(default=0)

    def seats_left(self):
        return self.total_seats - self.booked_seats
    
    def is_sold_out(self):
        return self.seats_left() <= 0
    
    def __str__(self):
        return self.title


class Booking(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE,related_name='bookings')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    seats_booked = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"
    


