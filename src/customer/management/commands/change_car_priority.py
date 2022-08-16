import random

from django.core.management.base import BaseCommand

from src.core.cars_data import customer_list
from src.customer.models import Customer
from src.car.models import Car


def change_car_priority():
    for customer in Customer.objects.all():
        cars = Car.objects.filter(dealer=None, customer=None)

        if len(cars) == 0:
            continue

        random_car = random.choice(cars)

        customer.car_priority=dict(
            brand=random_car.brand,
            car_model=random_car.car_model,
            body_type=random_car.body_type,
            year=random_car.year,
            transmission=random_car.transmission,
            fuel=random_car.fuel,
            engine_capacity=random_car.engine_capacity,
            mileage=999999,
            color=random_car.color,
            price=999999,
        )
        customer.save(update_fields=["car_priority"])


class Command(BaseCommand):
    help = u'Add customers'

    def handle(self, *args, **options):
        change_car_priority()
        return 'Customers added'