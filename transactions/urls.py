from django.urls import path, include
from rest_framework import routers

from transactions.views import *

router = routers.DefaultRouter()
router.register(r'showroom_customer_deals', ShowroomCustomerDealsViewSet)
router.register(r'dealer_showroom_deals', DealerShowroomDealsViewSet)

urlpatterns = [path("", include(router.urls))]