from rest_framework import viewsets
from src.customer.serializers import *
from src.customer.models import Customer
from rest_framework.permissions import IsAuthenticated
#from src.core.permissions import IsOwnerOrReadOnly


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, )
