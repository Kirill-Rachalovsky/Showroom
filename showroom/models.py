import datetime
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from dealer.models import Car, Dealer


class Showroom(models.Model):
    """Showroom"""

    name = models.CharField(
        max_length=50,
        verbose_name='Showroom Name',
        unique=True
    )
    description = models.TextField(
        blank=True,
        help_text='<i>More information about your company...</i>'
    )
    country = CountryField(blank_label='(select country)')
    start_year = models.DateField(default=datetime.datetime.now().year)
    balance = models.PositiveIntegerField(
        'Balance',
        default=1000000,
        help_text='<i>Put your balance in dollars</i>'
    )
    price_increase = models.PositiveSmallIntegerField(
        default=30,
        validators=[MaxValueValidator(500), MinValueValidator(1)],
        help_text='<b>Enter the markup on the cars you sell</b>',
    )
    slug = models.SlugField(max_length=100, unique=True)
    cars_options = models.JSONField(verbose_name='Car priority')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Showroom'
        verbose_name_plural = 'Showrooms'


class ShowroomDiscount(models.Model):
    """Discount"""

    organization = models.ForeignKey(Showroom, on_delete=models.CASCADE)
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


class DealerShowroomDeals(models.Model):
    """Dealer --> Showroom deals"""

    buyer = models.ForeignKey(Showroom, on_delete=models.PROTECT)
    seller = models.ForeignKey(Dealer, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Dealer --> Showroom deal'
        verbose_name_plural = 'Dealer --> Showroom deals'
