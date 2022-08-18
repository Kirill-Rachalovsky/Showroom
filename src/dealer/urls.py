from django.urls import path, include
from rest_framework import routers

from src.dealer.views import *

router = routers.DefaultRouter()
router.register(r'list', DealerViewSet)
router.register(r'detail', DealerDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
