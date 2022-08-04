from django.urls import path, include
from rest_framework import routers
from src.customer.views import *

router = routers.DefaultRouter()
router.register(r'list', CustomerViewSet)
router.register(r'detail', CustomerDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
