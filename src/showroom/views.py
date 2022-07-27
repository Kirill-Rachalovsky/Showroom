from rest_framework import viewsets
from src.showroom.serializers import *
from src.showroom.models import *


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomListSerializer


class ShowroomDetailViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomDetailSerializer


class ShowroomDiscountViewSet(viewsets.ModelViewSet):
    queryset = ShowroomDiscount.objects.all()
    serializer_class = ShowroomDiscountSerializer
