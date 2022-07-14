from django.contrib import admin
from .models import Customer, ShowroomCustomerDeals

admin.site.register(Customer)
admin.site.register(ShowroomCustomerDeals)

"""
@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    readonly_fields = ()
    list_filter = ()
"""