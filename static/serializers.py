from rest_framework import serializers
from showroom.models import Showroom
from transactions.models import *


class DealerDiscountSerializer(serializers.ModelSerializer):

    deals_amount = serializers.ReadOnlyField()
    personal_discount = serializers.ReadOnlyField()

    class Meta:
        model = DealerShowroomDeals
        fields = [
            'id',
            'buyer',
            'seller',
            'car',
            'deals_amount',
            'personal_discount'
        ]


class ShowroomDiscountSerializer(serializers.ModelSerializer):

    deals_amount = serializers.ReadOnlyField()
    personal_discount = serializers.ReadOnlyField()

    class Meta:
        model = ShowroomCustomerDeals
        fields = [
            'id',
            'buyer',
            'seller',
            'car',
            'deals_amount',
            'personal_discount'
        ]