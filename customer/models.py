from django.db import models
from static.abstractmodels import *
from django.contrib.auth.models import AbstractUser


class Customer(CustomerMixin, DataMixin, IsActivMixin, models.Model):
    """Customer"""

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    username = models.CharField(
        max_length=50,
        unique=True,
        help_text='<i>Put your unique username</i>'
    )
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)

