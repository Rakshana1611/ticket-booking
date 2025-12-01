from django.db import models

# Create your models here.
from django.db import models

class Flight(models.Model):
    company = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_no = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=50)
    flight_date = models.CharField(max_length=50)
    price = models.IntegerField()


class Booking(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    aadhaar = models.CharField(max_length=20)
    age = models.IntegerField()
    seat_class = models.CharField(max_length=50)
    seat_number = models.CharField(max_length=20)

