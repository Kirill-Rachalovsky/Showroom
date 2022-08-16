from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from src.car.models import Car
from src.car.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser,)