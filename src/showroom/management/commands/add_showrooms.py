from django.core.management.base import BaseCommand

from src.core.cars_data import *
from src.showroom.models import *
from src.dealer.models import Car


def add_showrooms():
    for showroom in showroom_list:

        car_options = []
        for i in range(5):
            car_options.append(get_random_car())

        Showroom.objects.create(
            name=showroom,
            description=f"Some description of {showroom}",
            country=get_random_country(),
            start_year=get_random_year(),
            car_priority=car_options
        )

    print("Showrooms added")


def add_discounts():
    showrooms = Showroom.objects.all()
    for instance in showrooms:
        ShowroomPersonalDiscount.objects.create(
            amount=random.randint(3,12),
            discount=random.randint(3,30),
            organization=instance
        )
    print("Discounts added")


def add_discounts_cars():
    showrooms = Showroom.objects.all()
    for showroom in showrooms:
        if len(showroom.showrooms_cars.all()) > 0:
            showrooms_cars_id = list(showroom.showrooms_cars.all().values('id'))
            limit = int(len(showrooms_cars_id)) - 1
            id_position_set = set()
            for i in range(random.randint(0, limit)):
                id_position_set.add(random.randint(0, limit))

            for id_position in id_position_set:
                ShowroomDiscountsCars.objects.create(
                    dealer=showroom,
                    car=Car.objects.get(id=showrooms_cars_id[id_position]["id"]),
                    percent=random.randint(1,12)
                )
    print("Discounts for cars added")


class Command(BaseCommand):
    help = u'Add Showrooms'

    def handle(self, *args, **options):
        add_showrooms()
        add_discounts()
        add_discounts_cars()
        return 'Showrooms and discounts added'
