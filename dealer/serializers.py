from rest_framework import serializers
from .models import Dealer, Car


class CarSerializer(serializers.ModelSerializer):

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
            'mileage',
            'is_new_car',
            'color',
            'price',
            'dealer',
        )


class DealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealer
        fields = (
            'organization_name',
            'description',
            'country',
            'start_year',
            'slug',
        )
