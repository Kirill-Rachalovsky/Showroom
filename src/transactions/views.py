from rest_framework import viewsets
from src.transactions.serializers import *
from src.core.permissions import IsAdminOrReadOnly


class ShowroomCustomerDealsViewSet(viewsets.ModelViewSet):
    queryset = ShowroomCustomerDeals.objects.all()
    serializer_class = ShowroomCustomerDealsSerializer
    permission_classes = (IsAdminOrReadOnly, )


class DealerShowroomDealsViewSet(viewsets.ModelViewSet):
    queryset = DealerShowroomDeals.objects.all()
    serializer_class = DealerShowroomDealsSerializer
    permission_classes = (IsAdminOrReadOnly, )

