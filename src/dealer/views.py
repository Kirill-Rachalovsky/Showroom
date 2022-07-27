from rest_framework import viewsets
from src.dealer.models import *
from src.dealer.serializers import *


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerListSerializer


class DealerDetailViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerDetailSerializer


class DealerDiscountViewSet(viewsets.ModelViewSet):
    queryset = DealerDiscount.objects.all()
    serializer_class = DealerDiscountSerializer
