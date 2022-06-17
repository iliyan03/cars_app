from rest_framework import viewsets

from .models import CarAd
from .serializers import CarSerializer

from .get_cars_ads.main import get_cars

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = CarAd.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        self.queryset._raw_delete(self.queryset.db)
        for x in get_cars():
            CarAd.objects.create(**x)
            
        return super().list(request, *args, **kwargs)

