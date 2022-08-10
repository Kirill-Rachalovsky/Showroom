from rest_framework import viewsets
from src.showroom.serializers import *
from src.showroom.models import *
from rest_framework.permissions import IsAdminUser
from src.core.permissions import *
from src.showroom.filters import *


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomListSerializer
    permission_classes = (IsAdminOrReadOnly, )
    filterset_class = ShowroomFilter


class ShowroomDetailViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomDetailSerializer
    permission_classes = (IsAdminUser, )
    filterset_class = ShowroomFilter


class ShowroomDiscountViewSet(viewsets.ModelViewSet):
    queryset = ShowroomPersonalDiscount.objects.all()
    serializer_class = ShowroomPersonalDiscountSerializer
    permission_classes = (IsAdminOrReadOnly, )
