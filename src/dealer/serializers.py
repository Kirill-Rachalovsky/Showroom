from rest_framework import serializers
from django.db.models import Count
from src.dealer.models import *
from src.transactions.serializers import *


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


class DealerPersonalDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerPersonalDiscount
        fields = (
            'amount',
            'discount',
        )


class DealerListSerializer(serializers.ModelSerializer):
    dealers_cars = CarSerializer(many=True, read_only=True)
    discount = serializers.SerializerMethodField()
    amount_buyers = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()


    class Meta:
        model = Dealer
        fields = (
            'name',
            'description',
            'amount_buyers',
            'total_sales',
            'country',
            'start_year',
            'dealers_cars',
            'discount',
        )

    def get_discount(self, obj):
        dealer_obj = Dealer.objects.get(id=obj.id)
        queryset = (
            dealer_obj
            .discounts
            .filter(is_active=True)
        )
        serializer = DealerPersonalDiscountSerializer(queryset, many=True).data
        return serializer

    def get_amount_buyers(self, obj):
        dealer_obj = Dealer.objects.get(id=obj.id)
        amount_buyers = (
            dealer_obj.sales_history.all()
            .values('buyer')
            .distinct()
            .count()
        )
        return amount_buyers

    def get_total_sales(self, obj):
        total = (
            Dealer.objects.get(id=obj.id)
            .sales_history
            .all()
            .count()
        )
        return total


class DealerDetailSerializer(serializers.ModelSerializer):
    dealers_cars = CarSerializer(many=True, read_only=True)
    amount_buyers = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()
    sales_history = serializers.SerializerMethodField()

    class Meta:
        model = Dealer
        fields = (
            'id',
            'name',
            'description',
            'country',
            'start_year',
            'is_active',
            'dealers_cars',
            'amount_buyers',
            'discount',
            'sales_history'
        )

    def get_amount_buyers(self, obj):
        dealer_obj = Dealer.objects.get(id=obj.id)
        amount_buyers = (
            dealer_obj.sales_history.all()
            .values('buyer')
            .distinct()
            .count()
        )
        return amount_buyers

    def get_discount(self, obj):
        dealer_obj = Dealer.objects.get(id=obj.id)
        queryset = (
            dealer_obj
            .discounts
            .filter(is_active=True)
        )
        serializer = DealerPersonalDiscountSerializer(queryset, many=True).data
        return serializer

    def get_sales_history(self, obj):
        dealer_obj = Dealer.objects.get(id=obj.id)
        queryset = (
            dealer_obj
            .sales_history
            .values('buyer__name')
            .annotate(number_of_transactions=Count('buyer'))
        )
        serializer_data = DealerShowroomDealsSerializer(queryset, many=True).data
        return serializer_data
