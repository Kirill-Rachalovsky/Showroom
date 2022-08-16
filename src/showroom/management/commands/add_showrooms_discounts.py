import random

from django.core.management.base import BaseCommand

from src.car.models import Car
from src.showroom.models import *


def add_discounts_cars():
    showrooms = Showroom.objects.all()
    for showroom in showrooms:
        showrooms_cars_id = list(showroom.showrooms_cars.all().values('id'))

        if len(showrooms_cars_id) == 0:
            continue

        limit = int(len(showrooms_cars_id)) - 1
        id_position_set = set()
        for i in range(random.randint(0, limit)):
            id_position_set.add(random.randint(0, limit))

        for id_position in id_position_set:
            ShowroomDiscountsCars.objects.create(
                showroom=showroom,
                car=Car.objects.get(id=showrooms_cars_id[id_position]["id"]),
                percent=random.randint(1,12)
            )
    print("Discounts for cars added")


class Command(BaseCommand):
    help = u'Add dealers and cars'

    def handle(self, *args, **options):
        add_discounts_cars()
        return 'Dealers and cars added'