import random

from django.core.management.base import BaseCommand
from src.core.cars_data import cars_models
from src.dealer.models import Dealer, Car
from src.core.cars_data import *


def add_dealers():
    for brand in cars_models:
        Dealer.objects.create(
            name=f"{brand} Dealer",
            description=f"We sell {brand} brand cars",
            country=get_random_country(),
            start_year=get_random_year(),
        )

    print("Dealers added")


def add_cars():
    for brand in cars_models:
        for i in range(3):
            Car.objects.create(
                brand=brand,
                cars_model=random.choice(list(cars_models[brand])),
                body_type=get_random_body_type(),
                year=get_random_year(),
                transmission=get_random_transmission(),
                fuel=get_random_fuel(),
                engine_capacity=(random.randint(10, 60)/10),
                color=get_random_color(),
                mileage =random.randint(0, 200000),
                price=random.randint(5000, 100000),
                dealer=Dealer.objects.get(name=f"{brand} Dealer")
            )

    print("Cars added")


class Command(BaseCommand):
    help = u'Add dealers for everybody'

    def handle(self, *args, **options):
        add_dealers()
        return 'Done'
