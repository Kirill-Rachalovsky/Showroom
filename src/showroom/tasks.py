from celery import shared_task
from django.db import transaction

from src.showroom.models import Showroom
from src.showroom.management.commands.add_showrooms_discounts import add_discounts_cars
from src.dealer.models import *
from src.car.models import *
from src.transactions.models import DealerShowroomDeals


@shared_task
def dealer_showroom_offer():
    for showroom in Showroom.objects.all():
        for car_info in showroom.car_priority:
            car_list = Car.objects.filter(
                brand=car_info['brand'],
                car_model=car_info['car_model'],
                showroom=None,
                customer=None,
            )

            if len(car_list) == 0:
                continue

            offers_with_discount = dict()

            for car in car_list:
                discount = 0
                loyality = 0

                total_deals = (
                    DealerShowroomDeals
                    .objects
                    .filter(buyer=showroom, seller=car.dealer, car=car.id)
                ).count()

                loyalty_program = car.dealer.discounts.first()

                if total_deals > loyalty_program.amount:
                    loyality = loyalty_program.discount

                try:
                    discount_obj = DealerDiscountsCars.objects.get(id=car_info[0].id)
                    if (discount_obj.dealer == car.dealer):
                        discount = discount_obj.percent
                except:
                    discount = 0

                total_discount = max(loyality, discount)
                total_price = int(car.price * (100 - total_discount) / 100)
                offers_with_discount[car.id] = total_price

            best_price = min(offers_with_discount.values())

            top_offer_id = 0
            for offer in offers_with_discount:
                if offers_with_discount[offer] == best_price:
                    top_offer_id = offer
                    break

            best_offer = Car.objects.get(id=top_offer_id)

            with transaction.atomic():
                if showroom.balance >= best_price:
                    DealerShowroomDeals.objects.create(
                        buyer=showroom,
                        seller=best_offer.dealer,
                        car=best_offer,
                        total_price=best_price
                    )

                    best_offer.dealer.total_sales += 1
                    best_offer.dealer.save(update_fields=["total_sales"])
                    best_offer.dealer = None
                    best_offer.showroom = showroom
                    best_offer.price = int(best_price * (100 + showroom.price_increase) / 100)
                    best_offer.save(update_fields=["dealer", "showroom", "price"])
                    showroom.balance -= best_price
                    showroom.save(update_fields=["balance"])


@shared_task
def add_cars_discounts():
    add_discounts_cars()
