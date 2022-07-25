from rest_framework import serializers
from showroom.models import *
from django.db.models import Q, F, Count

from transactions.serializers import *
from dealer.serializers import CarSerializer


class ShowroomDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomDiscount
        fields = (
            'amount',
            'discount',
            'data_start',
            'data_end',
        )


class ShowroomListSerializer(serializers.ModelSerializer):
    showrooms_cars = CarSerializer(many=True, read_only=True)
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
            'showrooms_cars',
            'discount',
        )

    def get_discount(self, obj):
        dealer_obj = Showroom.objects.get(id=obj.id)
        queryset = (
            dealer_obj
            .discounts
            .filter(is_active=True)
        )
        serializer = ShowroomDiscountSerializer(queryset, many=True).data
        return serializer

    def get_amount_buyers(self, obj):
        dealer_obj = Showroom.objects.get(id=obj.id)
        amount_buyers = (
            dealer_obj.sales_history.all()
            .values('buyer')
            .distinct()
            .count()
        )
        return amount_buyers

    def get_total_sales(self, obj):
        total = (
            Showroom.objects.get(id=obj.id)
            .sales_history
            .all()
            .count()
        )
        return total


class ShowroomDetailSerializer(serializers.ModelSerializer):
    showrooms_cars = CarSerializer(many=True, read_only=True)
    discount = serializers.SerializerMethodField()
    sales_history = serializers.SerializerMethodField()
    buying_history = serializers.SerializerMethodField()

    class Meta:
        model = Showroom
        fields = (
            'id',
            'organization_name',
            'description',
            'country',
            'start_year',
            'slug',
            'is_active',
            'balance',
            'user',
            'showrooms_cars',
            'discount',
            'sales_history',
            'buying_history',
        )

    def get_sales_history(self, obj):
        showroom_obj = Showroom.objects.get(id=obj.id)
        queryset = (
            showroom_obj
            .sales_history
            .values('buyer__username')
            .annotate(number_of_transactions=Count('buyer'))
        )
        serializer_data = ShowroomCustomerDealsSerializer(queryset, many=True).data
        return serializer_data

    def get_discount(self, obj):
        dealer_obj = Showroom.objects.get(id=obj.id)
        queryset = (
            dealer_obj
            .discounts
            .filter(is_active=True)
        )
        serializer = ShowroomDiscountSerializer(queryset, many=True).data
        return serializer

    def get_buying_history(self, obj):
        showroom_obj = Showroom.objects.get(id=obj.id)
        queryset =(
            showroom_obj
            .buying_history
            .values('seller__organization_name')
            .annotate(number_of_transactions=Count('buyer'))
        )
        serializer_data = ShowroomBuyingHistorySerializer(queryset, many=True).data
        return serializer_data

