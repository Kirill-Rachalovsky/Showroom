from django.contrib import admin
from src.dealer.models import *


@admin.register(DealerDiscount)
class DealerDiscountAdmin(admin.ModelAdmin):
    list_filter = (
        "data_start",
        "data_end",
        "amount",
        "discount",
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "brand",
        "car_model",
        "description",
        "body_type",
        "year",
        "transmission",
        "fuel",
        "engine_capacity",
        "mileage",
        "color",
        "is_new_car",
        "price",
        "dealer",
        "showroom",
        "customer",
    )
    list_filter = (
        "brand",
        "body_type",
        "year",
        "transmission",
        "fuel",
        "color",
        "is_new_car",
        "price",
    )
    search_fields = (
        "brand",
        "car_model",
        "body_type",
        "year",
        "transmission",
        "color",
    )


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
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
        dealer_obj = Dealer.objects.get(id=obj.id)
        amount = (
            dealer_obj.sales_history.all()
            .values('buyer')
            .distinct()
            .count()
        )
        return amount

    def total_sales(self, obj):
        total = (
            Dealer.objects.get(id=obj.id)
            .sales_history
            .all()
            .count()
        )
        return total
