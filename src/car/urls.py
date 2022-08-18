from django.urls import path, include
from rest_framework import routers

from src.car.views import CarViewSet

router = routers.DefaultRouter()
router.register(r'car', CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
