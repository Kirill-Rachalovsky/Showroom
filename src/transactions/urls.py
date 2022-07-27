from django.urls import path, include
from rest_framework import routers

from src.transactions.views import *

router = routers.DefaultRouter()
router.register(r'showroom_customer', ShowroomCustomerDealsViewSet)
router.register(r'dealer_showroom', DealerShowroomDealsViewSet)

urlpatterns = [
    path("", include(router.urls))
]
