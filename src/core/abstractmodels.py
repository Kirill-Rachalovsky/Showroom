from django.contrib.postgres.fields import DecimalRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime
import django.utils.timezone as timezone
from django_countries.fields import CountryField


def default_showroom_priorities():
    return {"brand": "Tesla",
            "car_model": "Model S",
            "color": "Black",
            "year": "2020",
            "body_type": "Sedan"}


class DataMixin(models.Model):
    """Adding creation and update dates"""

    data_creation = models.DateField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IsActivMixin(models.Model):
    """Status 'is_active' added"""

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class OrganizationsMixin(models.Model):
    """Common information about Showrooms and Dealers"""

    YEAR_CHOICES = []

    for r in range(2000, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    name = models.CharField(
        'Organization Name',
        max_length=50,
        unique=True
    )
    description = models.TextField(
        'Description',
        blank=True,
        help_text='<i>More information about your company...</i>'
    )
    country = CountryField(blank_label='(select country)')
    start_year = models.IntegerField(
        "Year",
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )

    class Meta:
        abstract = True


class CustomerMixin(models.Model):
    """Common information about Customers and Showrooms"""

    balance = models.PositiveIntegerField(
        'Balance',
        default=0,
        help_text='<i>Put your balance in dollars</i>'
    )
    # Сar search options
    car_priority = models.JSONField(
        encoder=None,
        decoder=None,
        default=default_showroom_priorities
    )

    class Meta:
        abstract = True


class DiscountMixin(models.Model):
    """Discount information"""

    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)],
        help_text='How many cars do I need to buy for the discount?'
    )
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text='Enter the size of the discount in percent',
    )
    data_start = models.DateField()
    data_end = models.DateField(default=datetime.datetime.now().date() + datetime.timedelta(days=30))

    def __str__(self):
        return f'Buy {self.amount} car to get a {self.discount}% discount for next cars!'

    class Meta:
        abstract = True
