from rest_framework import serializers
from dealer.models import *
from transactions.models import *
from django.db.models import Q, F, Count
from transactions.serializers import DealerShowroomDealsSerializer


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


class DealerDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerDiscount
        fields = (
            'amount',
            'discount',
            'data_start',
            'data_end',
        )


class DealerListSerializer(serializers.ModelSerializer):
    dealers_cars = CarSerializer(many=True, read_only=True)
    discount = serializers.SerializerMethodField()
    amount_buyers = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()

    class Meta:
        model = Dealer
        fields = (
            'organization_name',
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
        serializer = DealerDiscountSerializer(queryset, many=True).data
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
            'organization_name',
            'description',
            'country',
            'start_year',
            'slug',
            'is_active',
            'user',
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
        serializer = DealerDiscountSerializer(queryset, many=True).data
        return serializer

    def get_sales_history(self, obj):
        dealer_obj = Dealer.objects.get(id=obj.id)
        queryset = (
            dealer_obj
            .sales_history
            .values('buyer__organization_name')
            .annotate(number_of_transactions=Count('buyer'))
        )
        serializer_data = DealerShowroomDealsSerializer(queryset, many=True).data
        return serializer_data
