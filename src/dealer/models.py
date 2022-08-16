from src.core.abstractmodels import *
from django.db import models
from django.core.validators import MinValueValidator


class Dealer(OrganizationsMixin, DataMixin, IsActivMixin):
    """Dealer"""

    total_sales = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class DealerPersonalDiscount(PersonalDiscountMixin, IsActivMixin):
    """Discount"""

    organization = models.ForeignKey(
        'dealer.Dealer',
        on_delete=models.CASCADE,
        related_name='discounts'
    )

    def __str__(self):
        return f'{self.organization}: "Buy {self.amount} car to get a {self.discount}% discount for next cars!"'

    class Meta:
        verbose_name = 'Personal Discount'
        verbose_name_plural = 'Personal Discounts'


class DealerDiscountsCars(DiscountsCarsMixin):

    dealer = models.ForeignKey(
        'dealer.Dealer',
        on_delete=models.CASCADE,
        related_name='car_discounts'
    )
    car = models.ForeignKey(
        "car.Car",
        on_delete=models.CASCADE,
        related_name="discount_dealer_cars"
    )

    def __str__(self):
        return f'{self.car} has {self.percent} percent off in {self.dealer}!'

    class Meta:
        verbose_name = 'Cars Discount'
        verbose_name_plural = 'Cars Discounts'
