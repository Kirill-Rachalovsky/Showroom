from django_filters import rest_framework as filters

from src.dealer.models import Dealer


class DealerFilter(filters.FilterSet):
    class Meta:
        model = Dealer
        fields = {
            "name": ["icontains"],
            "country": ["icontains"],
            "start_year": ["exact", "lt", "gt"],
            "total_sales": ["exact", "lt", "gt"],
        }