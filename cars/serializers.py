from .models import CarAd
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = CarAd
        fields = ['url', 'date', 'link', 'img', 'price', 'model', 'description', 'comment', 'seller']