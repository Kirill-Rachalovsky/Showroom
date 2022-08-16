from django.db import models

from src.core.abstractmodels import TransactionMixin


class ShowroomCustomerDeals(TransactionMixin):
    """Showroom  --> Customer deals"""

    buyer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.PROTECT,
        related_name='buying_history'
    )
    seller = models.ForeignKey(
        'showroom.Showroom',
        on_delete=models.PROTECT,
        related_name='sales_history'
    )
    car = models.ForeignKey(
        'car.Car',
        on_delete=models.PROTECT,
        related_name='car_info'
    )
    deal_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Showroom  --> Customer deal'
        verbose_name_plural = 'Showroom  --> Customer deals'

    def __str__(self):
        return f'{self.seller} --> {self.buyer}, auto "{self.car}"'


class DealerShowroomDeals(TransactionMixin):
    """Dealer --> Showroom deals"""

    buyer = models.ForeignKey(
        'showroom.Showroom',
        on_delete=models.PROTECT,
        related_name='buying_history'
    )
    seller = models.ForeignKey(
        'dealer.Dealer',
        on_delete=models.PROTECT,
        related_name='sales_history'
    )
    car = models.ForeignKey(
        'car.Car',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Dealer --> Showroom deal'
        verbose_name_plural = 'Dealer --> Showroom deals'

    def __str__(self):
        return f'{self.seller} --> {self.buyer}, auto "{self.car}"'
