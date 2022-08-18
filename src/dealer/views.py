from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from src.core.permissions import *
from src.dealer.filters import *
from src.dealer.serializers import *


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


class DealerPersonalDiscountViewSet(viewsets.ModelViewSet):
    queryset = DealerPersonalDiscount.objects.all()
    serializer_class = DealerPersonalDiscountSerializer
    permission_classes = (IsAdminOrReadOnly,)
