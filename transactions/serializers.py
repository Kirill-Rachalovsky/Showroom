from rest_framework import serializers
from transactions.models import *
from dealer.models import Car
from showroom.models import Showroom


class ShowroomCustomerDealsSerializer(serializers.ModelSerializer):
    buyer__username = serializers.CharField()
    number_of_transactions = serializers.IntegerField()

    class Meta:
        model = DealerShowroomDeals
        fields = (
            'buyer__username',
            'number_of_transactions',
        )


class DealerShowroomDealsSerializer(serializers.ModelSerializer):
    buyer__organization_name = serializers.CharField()
    number_of_transactions = serializers.IntegerField()

    class Meta:
        model = DealerShowroomDeals
        fields = (
            'buyer__organization_name',
            'number_of_transactions',
        )


class ShowroomBuyingHistorySerializer(serializers.ModelSerializer):
    seller__organization_name = serializers.CharField()
    number_of_transactions = serializers.IntegerField()

    class Meta:
        model = DealerShowroomDeals
        fields = (
            'seller__organization_name',
            'number_of_transactions',
        )


class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'brand',
            'car_model',
            'body_type',
            'year',
            'transmission',
            'fuel',
            'engine_capacity',
            'color',
            'price',
        )


class ShowroomShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = (
            'organization_name',
        )


class CustomerBuyingHistorySerializer(serializers.ModelSerializer):
    seller = ShowroomShortInfoSerializer(read_only=True)
    car = CarInfoSerializer(read_only=True)

    class Meta:
        model = ShowroomCustomerDeals
        fields = (
            'seller',
            'car',
        )


class CustomerBuyingStatisticSerializer(serializers.ModelSerializer):
    seller__organization_name = serializers.CharField()
    number_of_transactions = serializers.IntegerField()

    class Meta:
        model = DealerShowroomDeals
        fields = (
            'seller__organization_name',
            'number_of_transactions',
        )
