from rest_framework import viewsets
from src.customer.serializers import *
from src.customer.models import Customer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from src.core.permissions import IsAdminOrIsOwner, IsAdminOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdminOrReadOnly, )
    search_fields = ("username",)


class CustomerDetailViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
    # permission_classes = [(IsAuthenticated | IsAdminUser)]
    permission_classes = (IsAdminOrIsOwner, )
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("username",)
