from django.urls import include, path
from rest_framework import routers

from .views import CarViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]