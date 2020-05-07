from django.db import models

# Create your models here.
class District(models.Model):
    code = models.CharField(max_length=5)
    place = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.place} ({self.code})"

class Bus(models.Model):
    origin = models.ForeignKey(District, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(District, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    journeys = models.ManyToManyField(Bus, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
