from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CompetitorPriceViewSet, PriceHistoryViewSet, DemandForecastViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'competitor-prices', CompetitorPriceViewSet)
router.register(r'price-history', PriceHistoryViewSet)
router.register(r'demand-forecasts', DemandForecastViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
