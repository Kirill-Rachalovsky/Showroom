from django.contrib import admin
from src.customer.models import Customer


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = (
        "username",
        "balance",
        "data_creation",
        "is_active",
    )
    list_editable = (
        "is_active",
    )
    readonly_fields = (
        "data_creation",
        "data_update",
        "balance",
        "total_deals",
    )
    list_filter = (
        "data_creation",
        "data_update",
    )

    def total_deals(self, obj):
        customer_obj = Customer.objects.get(id=obj.id)
        total = (
            customer_obj
            .buying_history
            .all()
            .count()
        )
        return total
