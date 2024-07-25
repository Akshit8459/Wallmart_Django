from rest_framework import serializers
from .models import Supplier, DeliveryRoute, EmissionData

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class DeliveryRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRoute
        fields = '__all__'

class EmissionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionData
        fields = '__all__'
