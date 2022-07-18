from django.db import models
from static.abstractmodels import *
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Car(models.Model):
    """Car options"""

    BODY_CHOICES = [
        (None, 'Select the car body type'),
        (1, 'SUV'),
        (2, 'Sedan'),
        (3, 'Сoupe'),
        (4, 'Wagon'),
        (5, 'Minivan'),
        (6, 'Hatchback'),
        (7, 'Liftback'),
        (8, 'Limousine'),
        (9, 'Cabriolet'),
        (10, 'Another')
    ]

    TRANSMISSION_CHOICES = [
        (None, 'Select transmission type'),
        (1, 'Manual'),
        (2, 'Automatic'),
    ]

    FUEL_CHOICER = [
        (None, 'Select fuel type'),
        (1, 'Petrol'),
        (2, 'Diesel'),
        (3, 'Gas'),
        (4, 'Electric'),
        (5, 'Hybrid'),
    ]

    YEAR_CHOICES = []

    for r in range(2000, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    brand = models.CharField(
        'Car Brand',
        max_length=50,
        help_text="<i>Put the car's brand</i>"
    )
    car_model = models.CharField(
        'Car Model',
        max_length=50,
        help_text="<i>Put the car's model</i>"
    )
    description = models.TextField(
        blank=True,
        help_text='<i>More information about the car...</i>'
    )
    body_type = models.IntegerField(
        "Body type",
        choices=BODY_CHOICES
    )
    year = models.IntegerField(
        "Year",
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )
    transmission = models.IntegerField(
        "Transmission",
        choices=TRANSMISSION_CHOICES
    )
    fuel = models.IntegerField(
        'Fuel type',
        choices=FUEL_CHOICER,
    )
    engine_capacity = models.FloatField(
        "Engine capacity",
        null=True
    )
    mileage = models.IntegerField(
        "Car mileage",
        null=True
    )
    is_new_car = models.BooleanField(
        "New car",
        default=False
    )
    color = models.CharField(max_length=25, verbose_name='Colour')
    price = models.PositiveIntegerField(
        "Price",
        validators=[MinValueValidator(0)],
        default=0,
        help_text="<i>Enter the price in dollars</i>"
    )
    showroom = models.ForeignKey(
        "showroom.Showroom",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="showrooms_cars",
    )
    dealer = models.ForeignKey(
        "Dealer",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="dealers_cars",
    )
    customer = models.ForeignKey(
        "customer.Customer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customers_cars",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.car_model} | year:{self.year} | mileage:{self.mileage}'

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Dealer(OrganizationsMixin, DataMixin, IsActivMixin, models.Model):
    """Dealer"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class DealerDiscount(DiscountMixin, IsActivMixin, models.Model):
    """Discount"""

    organization = models.ForeignKey('Dealer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'




