from rest_framework import serializers
from src.car.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'brand',
            'car_model',
            'description',
            'body_type',
            'year',
            'transmission',
            'fuel',
            'engine_capacity',
            'mileage',
            'is_new_car',
            'color',
            'price',
        )
