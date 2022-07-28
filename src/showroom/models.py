from src.core.abstractmodels import *
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Showroom(OrganizationsMixin, CustomerMixin, IsActivMixin, DataMixin, models.Model):
    """Showroom"""

    price_increase = models.PositiveSmallIntegerField(
        default=30,
        validators=[MaxValueValidator(500), MinValueValidator(1)],
        help_text='<b>Enter the markup on the cars you sell</b>',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Showroom'
        verbose_name_plural = 'Showrooms'


class ShowroomDiscount(DiscountMixin, IsActivMixin, models.Model):
    """Discount"""

    organization = models.ForeignKey(
        'showroom.Showroom',
        on_delete=models.CASCADE,
        related_name='discounts'

    )

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

