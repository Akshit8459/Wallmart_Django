# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_level = models.IntegerField()

    def __str__(self):
        return self.name


class CompetitorPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='competitor_prices')
    competitor_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.competitor_name} - {self.product.name}"


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.price} at {self.timestamp}"


class DemandForecast(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='demand_forecasts')
    predicted_demand = models.IntegerField()
    forecast_date = models.DateField()

    def __str__(self):
        return f"{self.product.name} - {self.predicted_demand} on {self.forecast_date}"
