from rest_framework import viewsets
from src.customer.serializers import *
from src.customer.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("username",)
