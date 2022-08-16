from django.core.management.base import BaseCommand

from src.core.cars_data import *
from src.dealer.models import *


def add_dealers():
    for brand in cars_models:
        Dealer.objects.create(
            name=f"{brand} Dealer",
            description=f"We sell {brand} brand cars",
            country=get_random_country(),
            start_year=get_random_year(),
        )
    print("Dealers added")


def add_discounts():
    dealers = Dealer.objects.all()
    for instance in dealers:
        DealerPersonalDiscount.objects.create(
            amount=random.randint(3,12),
            discount=random.randint(3,30),
            organization=instance
        )
    print("Discounts added")


# ДЛЯ ДОБАВЛЕНИЯ ВСЕХ МОДЕЛЕЙ

# def add_cars():
#     for brand in cars_models:
#         for model in cars_models[brand]:
#             Car.objects.create(
#                 brand=brand,
#                 car_model=model,
#                 body_type=get_random_body_type(),
#                 year=get_random_year(),
#                 transmission=get_random_transmission(),
#                 fuel=get_random_fuel(),
#                 engine_capacity=(random.randint(10, 60)/10),
#                 color=get_random_color(),
#                 mileage =random.randint(0, 200000),
#                 price=random.randint(5000, 100000),
#                 dealer=Dealer.objects.get(name=f"{brand} Dealer")
#             )
#     print("Cars added")


class Command(BaseCommand):
    help = u'Add dealers and cars'

    def handle(self, *args, **options):
        add_dealers()
        add_discounts()
        return 'Dealers and cars added'
