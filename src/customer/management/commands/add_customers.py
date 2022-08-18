import re

from django.core.management.base import BaseCommand

from src.core.cars_data import customer_list
from src.customer.models import Customer


def add_customers():
    for customer in customer_list:

        first_name = re.findall(r'\w+', customer)[0]
        last_name = re.findall(r'\w+', customer)[1]

        Customer.objects.create_user(
            username=customer.lower().replace(' ', '_'),
            first_name=first_name,
            last_name=last_name,
            password="1234",
        )


class Command(BaseCommand):
    help = u'Add customers'

    def handle(self, *args, **options):
        add_customers()
        return 'Customers added'

