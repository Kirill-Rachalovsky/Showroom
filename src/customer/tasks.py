from celery import shared_task
from django.db import transaction
from django.db.models import Q

from src.car.models import *
from src.customer.management.commands.change_car_priority import change_car_priority
from src.customer.models import *
from src.showroom.models import *
from src.transactions.models import ShowroomCustomerDeals


def find_best_offer(customer, car_list):
    offers_with_discount = dict()

    for car in car_list:
        discount = 0
        loyality = 0

        total_deals = (
            ShowroomCustomerDeals
            .objects
            .filter(buyer=customer, seller=car.showroom, car=car.id)
        ).count()

        loyalty_program = car.showroom.discounts.first()

        if total_deals > loyalty_program.amount:
            loyality = loyalty_program.discount

        try:
            discount_obj = ShowroomDiscountsCars.objects.get(car_id=car.id)
            if (discount_obj.showroom == car.showroom):
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

    return best_offer, best_price


def showroom_customer_offer():
    for customer in Customer.objects.all():

        customer_search = (
            Q(brand__icontains=customer.car_priority.get("brand"))
            & Q(car_model__icontains=customer.car_priority.get("car_model"))
            & Q(body_type__icontains=customer.car_priority.get("body_type"))
            & Q(year__gte=customer.car_priority.get("year"))
            & Q(transmission__icontains=customer.car_priority.get("transmission"))
            & Q(fuel__icontains=customer.car_priority.get("fuel"))
            & Q(engine_capacity__gte=customer.car_priority.get("engine_capacity"))
            & Q(mileage__lte=customer.car_priority.get("mileage"))
            & Q(color__icontains=customer.car_priority.get("color"))
            & Q(price__lte=customer.car_priority.get("price"))
        )

        car_list = Car.objects.filter(
            customer_search,
            dealer=None,
            customer=None,
        )

        if len(car_list) == 0:
            continue

        best_offer, best_price = find_best_offer(customer, car_list)

        with transaction.atomic():
            if customer.balance >= best_price:

                ShowroomCustomerDeals.objects.create(
                    buyer=customer,
                    seller=best_offer.showroom,
                    car=best_offer,
                    total_price=best_price
                )

                best_offer.showroom.total_sales += 1
                best_offer.showroom.save(update_fields=["total_sales"])
                best_offer.showroom = None
                best_offer.customer = customer
                best_offer.save(update_fields=["customer", "showroom"])
                customer.total_deals += 1
                customer.balance -= best_price
                customer.save(update_fields=["total_deals", "balance"])


@shared_task
def make_customer_offer():
    change_car_priority()
    showroom_customer_offer()
