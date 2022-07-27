from rest_framework import viewsets
from src.customer.serializers import *
from src.customer.models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
