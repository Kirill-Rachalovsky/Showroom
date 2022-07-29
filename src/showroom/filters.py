from django_filters import rest_framework as filters

from src.showroom.models import Showroom


class ShowroomFilter(filters.FilterSet):
    class Meta:
        model = Showroom
        fields = {
            "name": ["icontains"],
            "country": ["icontains"],
            "start_year": ["exact", "lt", "gt"],
            "total_sales": ["exact", "lt", "gt"],
        }
