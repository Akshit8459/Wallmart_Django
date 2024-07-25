from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('todos/',views.todos,name='todos'),
    path('suppliers/', views.SupplierViewSet),
    path('delivery_routes/', views.DeliveryRouteViewSet),
    path('emission_data/', views.EmissionDataViewSet),
]
