from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


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

    car_model = models.CharField(
        'Car Model',
        max_length=50,
        help_text="<i>Put the car's name</i>"
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
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
        verbose_name="Year"
    )
    transmission = models.IntegerField(
        choices=TRANSMISSION_CHOICES,
        verbose_name="Transmission"
    )
    fuel = models.IntegerField(
        choices=FUEL_CHOICER,
        verbose_name='Fuel type'
    )
    engine_capacity = models.FloatField(
        verbose_name="Engine capacity",
        null=True
    )
    mileage = models.IntegerField(
        verbose_name="Car mileage",
        null=True
    )
    is_new_car = models.BooleanField(
        default=False,
        verbose_name="New car"
    )
    default_price = models.PositiveIntegerField(
        "Price",
        validators=[MinValueValidator(1)],
        default=0,
        help_text="<i>Enter the price in dollars</i>"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.car_model} | year:{self.year} | mileage:{self.mileage}'

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Dealer(models.Model):
    """Dealer"""

    name = models.CharField(
        max_length=50,
        verbose_name='Name of dealer',
        unique=True
    )
    description = models.TextField(
        blank=True,
        help_text='<i>More information about your company...</i>'
    )
    start_year = models.DateField(default=datetime.datetime.now().year)
    slug = models.SlugField(max_length=100, unique=True)
    cars = models.ManyToManyField(Car, verbose_name="Dealer's cars")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class DealerDiscount(models.Model):
    """Discount"""

    organization = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)],
        help_text='How many cars do I need to buy for the discount?'
    )
    discount = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        help_text='Enter the size of the discount in percent',
    )
    data_start = models.DateField()
    data_end = models.DateField(default=datetime.datetime.now().date() + datetime.timedelta(days=30))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Buy {self.amount} car to get a {self.discount}% discount!'

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'




