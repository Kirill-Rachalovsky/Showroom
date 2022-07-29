from rest_framework import viewsets
from src.showroom.serializers import *
from src.showroom.models import *
from rest_framework.permissions import IsAdminUser
from src.core.permissions import *


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomListSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ShowroomDetailViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomDetailSerializer
    permission_classes = (IsAdminUser, )


class ShowroomDiscountViewSet(viewsets.ModelViewSet):
    queryset = ShowroomDiscount.objects.all()
    serializer_class = ShowroomDiscountSerializer
    permission_classes = (IsAdminOrReadOnly, )
