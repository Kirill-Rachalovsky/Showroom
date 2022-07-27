from django.contrib import admin
from src.transactions.models import *


@admin.register(ShowroomCustomerDeals)
class ShowroomCustomerDealsAdmin(admin.ModelAdmin):
    list_filter = (
        "deal_date",
    )


@admin.register(DealerShowroomDeals)
class DealerShowroomDealsAdmin(admin.ModelAdmin):
    list_filter = (
        "deal_date",
    )
