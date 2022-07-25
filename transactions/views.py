from rest_framework import viewsets

from transactions.serializers import *


class ShowroomCustomerDealsViewSet(viewsets.ModelViewSet):
    queryset = ShowroomCustomerDeals.objects.all()
    serializer_class = ShowroomCustomerDealsSerializer


class DealerShowroomDealsViewSet(viewsets.ModelViewSet):
    queryset = DealerShowroomDeals.objects.all()
    serializer_class = DealerShowroomDealsSerializer
