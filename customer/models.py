from django.db import models
from showroom.models import Showroom
from dealer.models import Car


class Customer(models.Model):
    """Customer"""

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    username = models.CharField(
        max_length=50,
        unique=True,
        help_text='<i>Put your unique username</i>'
    )
    email = models.EmailField(unique=True)
    balance = models.PositiveIntegerField(
        'Balance',
        default=100000,
        help_text='<i>Put your balance in dollars</i>'
    )
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)


class ShowroomCustomerDeals(models.Model):
    """Showroom  --> Customer deals"""

    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    seller = models.ForeignKey(Showroom, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Showroom  --> Customer deal'
        verbose_name_plural = 'Showroom  --> Customer deals'
