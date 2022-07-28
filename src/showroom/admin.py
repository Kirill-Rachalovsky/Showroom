from django.contrib import admin
from src.showroom.models import *


@admin.register(ShowroomDiscount)
class ShowroomDiscountAdmin(admin.ModelAdmin):
    list_filter = (
        "data_start",
        "data_end",
        "amount",
        "discount",
    )


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "start_year",
        "amount_buyers",
        "total_sales",
    )
    readonly_fields = (
        "data_creation",
        "data_update",
    )
    list_filter = (
        "country",
        "start_year",
    )
    search_fields = (
        "name",
        "country"
    )

    def amount_buyers(self, obj):
        dealer_obj = Showroom.objects.get(id=obj.id)
        amount = (
            dealer_obj.sales_history.all()
            .values('buyer')
            .distinct()
            .count()
        )
        return amount

    def total_sales(self, obj):
        total = (
            Showroom.objects.get(id=obj.id)
            .sales_history
            .all()
            .count()
        )
        return total
