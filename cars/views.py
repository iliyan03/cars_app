from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import CarAd
from .serializers import CarSerializer

from .get_cars_ads.main import get_cars

# Create your views here.

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarAd.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_queryset(self):
        refresh = self.request.query_params.get('refresh')
        if refresh is not None:
            self.queryset._raw_delete(self.queryset.db)
            for x in get_cars():
                CarAd.objects.create(**x)
            return CarAd.objects.all()
        return super().get_queryset()