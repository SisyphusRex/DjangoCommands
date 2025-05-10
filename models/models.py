from django.db import models

# Create Models Here
class Flight(models.Model):  # class is a child of django model
  origin = models.CharField(max_length=64)  # django models have predefined data types
  destination = models.Charfield(max_length=64)
  duration= models.IntegerField()

def __str__(self):
  return f"{self.id}: {self.origin} {self.destination}" # self.id need not be defined because django db will assign key as id
