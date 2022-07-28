from src.customer.models import *
from django.db.models import Count
from src.transactions.serializers import *


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
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
            .values('seller__name')
            .annotate(number_of_transactions=Count('seller__name'))
        )
        serializer_data = CustomerBuyingStatisticSerializer(queryset, many=True).data
        return serializer_data
