from django.urls import path, include
from rest_framework import routers

from dealer.views import *

router = routers.DefaultRouter()
router.register(r'dealer', DealerViewSet)
router.register(r'car', CarViewSet)
router.register(r'dealer/discount', DealerDiscountViewSet)
router.register(r'dealer/detail', DealerDetailViewSet)       # Для личного кабинета

urlpatterns = [
    path("", include(router.urls)),
]
