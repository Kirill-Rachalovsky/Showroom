from src.core.abstractmodels import *
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Showroom(OrganizationsMixin, CustomerMixin, IsActivMixin, DataMixin):
    """Showroom"""

    total_sales = models.PositiveIntegerField(default=0)
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


class ShowroomPersonalDiscount(PersonalDiscountMixin, IsActivMixin):
    """Discount"""

    organization = models.ForeignKey(
        'showroom.Showroom',
        on_delete=models.CASCADE,
        related_name='discounts'

    )

    def __str__(self):
        return f'{self.organization}: "Buy {self.amount} car to get a {self.discount}% discount for next cars!"'

    class Meta:
        verbose_name = 'Personal Discount'
        verbose_name_plural = 'Personal Discounts'


class ShowroomDiscountsCars(DiscountsCarsMixin):

    showroom = models.ForeignKey(
        'showroom.Showroom',
        on_delete=models.CASCADE,
        related_name='car_discounts'
    )
    car = models.ForeignKey(
        "car.Car",
        on_delete=models.CASCADE,
        related_name="discount_showroom_cars"
    )

    def __str__(self):
        return f'{self.car} has {self.percent} percent off in {self.showroom}!'

    class Meta:
        verbose_name = 'Cars Discount'
        verbose_name_plural = 'Cars Discounts'

