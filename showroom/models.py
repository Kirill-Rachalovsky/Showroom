import datetime
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from dealer.models import Car, Dealer
from static.abstractmodels import *
from django.contrib.auth.models import User


class Showroom(OrganizationsMixin, CustomerMixin, IsActivMixin, DataMixin, models.Model):
    """Showroom"""

    price_increase = models.PositiveSmallIntegerField(
        default=30,
        validators=[MaxValueValidator(500), MinValueValidator(1)],
        help_text='<b>Enter the markup on the cars you sell</b>',
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = 'Showroom'
        verbose_name_plural = 'Showrooms'


class ShowroomDiscount(DiscountMixin, IsActivMixin, models.Model):
    """Discount"""

    organization = models.ForeignKey(
        Showroom,
        on_delete=models.CASCADE,
        related_name='discounts'

    )

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

