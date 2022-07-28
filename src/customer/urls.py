from django.urls import path, include
from rest_framework import routers

from src.customer.views import *

router = routers.DefaultRouter()
router.register(r'', CustomerViewSet)

urlpatterns = [
    path("", include(router.urls))
]
