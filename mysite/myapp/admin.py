from django.contrib import admin
from .models import Product, CompetitorPrice, PriceHistory, DemandForecast

admin.site.register(Product)
admin.site.register(CompetitorPrice)
admin.site.register(PriceHistory)
admin.site.register(DemandForecast)
