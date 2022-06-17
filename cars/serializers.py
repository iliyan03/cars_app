from .models import CarAd
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarAd
        fields = '__all__'