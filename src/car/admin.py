from django.contrib import admin

from src.car.models import *


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
