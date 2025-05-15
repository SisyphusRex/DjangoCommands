from django.db import models

# Create Models Here
class Airport(models.model):
  code = models.CharField(max_length=3)
  city = models.CharField(max_length=64)

  def __str__(self):
    return f"{self.city}: ({self.code})"

class Flight(models.Model):  # class is a child of django model
  origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") # makes origin a foreign key, if foreign key (airport) deleted, delete flight 
  # related_name allows you to reverse look up all flights with airport as origin
  destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
  duration= models.IntegerField()

  def __str__(self):
    return f"{self.id}: {self.origin} {self.destination}" # self.id need not be defined because django db will assign key as id

class Passenger(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  # many to many: passenger can have multiple flights and flights have multiple passengers
  flights = models.ManyToManyField(
    Flight,
    blank=True,
    related_name="passengers",
  )
