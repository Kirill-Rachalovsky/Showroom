from django.shortcuts import render
from rest_framework import generics
from .models import Dealer
from .serializers import DealerSerializer


class DealerAPIView(generics.ListAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

