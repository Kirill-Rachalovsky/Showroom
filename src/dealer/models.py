from src.core.abstractmodels import *
from django.db import models
from django.core.validators import MinValueValidator


class Car(models.Model):
    """Car options"""

    BODY_CHOICES = [
        (None, 'Select the car body type'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Сoupe', 'Сoupe'),
        ('Wagon', 'Wagon'),
        ('Minivan', 'Minivan'),
        ('Hatchback', 'Hatchback'),
        ('Liftback', 'Liftback'),
        ('Limousine', 'Limousine'),
        ('Cabriolet', 'Cabriolet'),
        ('Another', 'Another')
    ]

    TRANSMISSION_CHOICES = [
        (None, 'Select transmission type'),
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    FUEL_CHOICER = [
        (None, 'Select fuel type'),
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Gas', 'Gas'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    COLOR_CHOICER = [
        (None, "Select car's color"),
        ('Red', 'Red'),
        ('Grey', 'Grey'),
        ('Light blue', 'Light blue'),
        ('Dark blue', 'Dark blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Pink', 'Pink'),
        ('Orange', 'Orange'),
        ('Brown', 'Brown'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Violet', 'Violet'),
    ]

    YEAR_CHOICES = []

    for r in range(1980, (datetime.datetime.now().year + 1)):
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
    body_type = models.CharField(
        "Body type",
        max_length=50,
        choices=BODY_CHOICES
    )
    year = models.CharField(
        "Year",
        max_length=50,
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )
    transmission = models.CharField(
        "Transmission",
        max_length=50,
        choices=TRANSMISSION_CHOICES
    )
    fuel = models.CharField(
        'Fuel type',
        max_length=50,
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
    color = models.CharField(
        'Color',
        max_length=20,
        choices=COLOR_CHOICER,
    )
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
        "dealer.Dealer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="dealers_cars",
    )
    customer = models.ForeignKey(
        "customer.Customer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customers_cars",
    )

    def __str__(self):
        return f'{self.brand} {self.car_model} | year:{self.year} | mileage:{self.mileage}'

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


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
        "dealer.Car",
        on_delete=models.CASCADE,
        related_name="discount_dealer_cars"
    )

    def __str__(self):
        return f'{self.car} has {self.percent} percent off in {self.dealer}!'

    class Meta:
        verbose_name = 'Cars Discount'
        verbose_name_plural = 'Cars Discounts'
