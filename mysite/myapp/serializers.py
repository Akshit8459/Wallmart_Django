# serializers.py
from rest_framework import serializers
from .models import Product, CompetitorPrice, PriceHistory, DemandForecast

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CompetitorPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitorPrice
        fields = '__all__'


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = '__all__'


class DemandForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandForecast
        fields = '__all__'
