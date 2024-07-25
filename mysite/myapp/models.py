from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    sustainability_score = models.FloatField()
    carbon_footprint = models.FloatField()  # e.g., kg CO2 per unit

class DeliveryRoute(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.FloatField()  # in kilometers
    estimated_emissions = models.FloatField()  # in kg CO2

class EmissionData(models.Model):
    route = models.ForeignKey(DeliveryRoute, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    emissions = models.FloatField()  # in kg CO2