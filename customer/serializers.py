from rest_framework import serializers
from .models import *
from django.db.models import Q, F, Count

from transactions.serializers import *
from dealer.serializers import CarSerializer


class CustomerSerializer(serializers.ModelSerializer):
    buying_history = serializers.SerializerMethodField()
    buying_statistic = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'second_name',
            'username',
            'balance',
            'buying_history',
            'buying_statistic',
            'slug',
            'user',
            'is_active',
        )

    def get_buying_history(self, obj):
        customer_obj = Customer.objects.get(id=obj.id)
        queryset = (
            customer_obj
            .buying_history
            .all()
        )
        serializer_data = CustomerBuyingHistorySerializer(queryset, many=True).data
        return serializer_data

    def get_buying_statistic(self, obj):
        customer_obj = Customer.objects.get(id=obj.id)
        queryset = (
            customer_obj
            .buying_history
            .values('seller__organization_name')
            .annotate(number_of_transactions=Count('seller__organization_name'))
        )
        for i in range(len(queryset)):
            i
        serializer_data = CustomerBuyingStatisticSerializer(queryset, many=True).data
        return serializer_data
