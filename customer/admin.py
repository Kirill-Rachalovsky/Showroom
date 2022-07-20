from django.contrib import admin
from .models import Customer

admin.site.register(Customer)

"""
@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    readonly_fields = ()
    list_filter = ()
"""