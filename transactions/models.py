from django.db import models
from django.db.models import Q, F
from dealer.models import DealerDiscount
from showroom.models import ShowroomDiscount


class ShowroomCustomerDeals(models.Model):
    """Showroom  --> Customer deals"""

    buyer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)
    seller = models.ForeignKey('showroom.Showroom', on_delete=models.PROTECT)
    car = models.ForeignKey('dealer.Car', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Showroom  --> Customer deal'
        verbose_name_plural = 'Showroom  --> Customer deals'

        # @property
        # def deals_amount(self):
        #     count = ShowroomCustomerDeals.objects.filter(Q(buyer == F('buyer')) & Q(seller == F('seller'))).count()
        #     return count
        #
        # @property
        # def personal_discount(self):
        #     discount_obj = ShowroomDiscount.objects.get(Q(organization == F('seller') | Q(is_active == True)))
        #     if self.deals_amount >= discount_obj.amount:
        #         return discount_obj.discount
        #     else:
        #         return 0


class DealerShowroomDeals(models.Model):
    """Dealer --> Showroom deals"""

    buyer = models.ForeignKey('showroom.Showroom', on_delete=models.PROTECT)
    seller = models.ForeignKey('dealer.Dealer', on_delete=models.PROTECT)
    car = models.ForeignKey('dealer.Car', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Dealer --> Showroom deal'
        verbose_name_plural = 'Dealer --> Showroom deals'

    # @property
    # def deals_amount(self):
    #     count = DealerShowroomDeals.objects.filter(Q(buyer ==F('buyer')) & Q(seller == F('seller'))).count()
    #     return count
    #
    # @property
    # def personal_discount(self):
    #     discount_obj = DealerDiscount.objects.get(Q(organization==F('seller') | Q(is_active==True)))
    #     if self.deals_amount >= discount_obj.amount:
    #         return discount_obj.discount
    #     else:
    #         return 0

