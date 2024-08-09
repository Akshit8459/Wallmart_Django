from rest_framework import viewsets
from .models import Product, CompetitorPrice, PriceHistory, DemandForecast
from .serializers import ProductSerializer, CompetitorPriceSerializer, PriceHistorySerializer, DemandForecastSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompetitorPriceViewSet(viewsets.ModelViewSet):
    queryset = CompetitorPrice.objects.all()
    serializer_class = CompetitorPriceSerializer


class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer


class DemandForecastViewSet(viewsets.ModelViewSet):
    queryset = DemandForecast.objects.all()
    serializer_class = DemandForecastSerializer
