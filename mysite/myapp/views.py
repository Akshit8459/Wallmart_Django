from django.shortcuts import render, HttpResponse
from .models import TodoItem,Supplier, DeliveryRoute, EmissionData
from .serializers import SupplierSerializer, DeliveryRouteSerializer, EmissionDataSerializer

# Create your views here.
def home(request):
    return render(request,'home.html')

def todos(request):
    items=TodoItem.objects.all()
    return render(request,'todos.html',{"todos":items}) 

def SupplierViewSet(# viewsets.ModelViewSet
request):
    '''this will be class not def'''
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    return HttpResponse('supplier portal')

def DeliveryRouteViewSet(
    # viewsets.ModelViewSet
     request):
    queryset = DeliveryRoute.objects.all()
    serializer_class = DeliveryRouteSerializer
    return HttpResponse('delivery route portal')

def EmissionDataViewSet(
    # viewsets.ModelViewSet
    request):
    queryset = EmissionData.objects.all()
    serializer_class = EmissionDataSerializer
    return HttpResponse('emission data portal')