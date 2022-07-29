from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.customer.models import Customer


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):

    list_display = (
        "id",
        "username",
        "balance",
        "is_active",
        "total_deals",
    )

    list_editable = (
        "is_active",
    )
    readonly_fields = (
        "balance",
        "total_deals",
    )

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            "Custom fields",
            {
                "fields": (
                    "balance",
                    "car_priority",
                    "total_deals",
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Custom fields",
            {
                "fields": (
                    "balance",
                    "car_priority",
                    "total_deals",
                )
            }
        )
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
