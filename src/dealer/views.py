from rest_framework import viewsets
from src.dealer.serializers import *
from rest_framework.permissions import IsAdminUser
from src.core.permissions import *
from rest_framework.filters import OrderingFilter, SearchFilter
from src.dealer.filters import *


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser,)


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerListSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = DealerFilter


class DealerDetailViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerDetailSerializer
    permission_classes = (IsAdminUser,)
    filterset_class = DealerFilter


class DealerDiscountViewSet(viewsets.ModelViewSet):
    queryset = DealerDiscount.objects.all()
    serializer_class = DealerDiscountSerializer
    permission_classes = (IsAdminOrReadOnly,)
