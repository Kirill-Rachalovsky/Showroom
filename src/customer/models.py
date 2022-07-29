from src.core.abstractmodels import *
from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(CustomerMixin, AbstractUser):
    """Customer"""

    username = models.CharField(
        max_length=50,
        unique=True,
        help_text='<i>Put your unique username</i>'
    )

    def __str__(self):
        return self.username
