from django.contrib import admin

from src.dealer.models import *


@admin.register(DealerPersonalDiscount)
class DealerDiscountAdmin(admin.ModelAdmin):
    list_filter = (
        "amount",
        "discount",
    )


@admin.register(DealerDiscountsCars)
class DealerDiscountsCars(admin.ModelAdmin):
    list_filter = (
        "dealer",
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
