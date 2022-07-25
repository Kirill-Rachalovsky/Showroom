from django.urls import path, include
from rest_framework import routers

from showroom.views import *

router = routers.DefaultRouter()
router.register(r'showroom', ShowroomViewSet)
router.register(r'showroom/discount', ShowroomDiscountViewSet)
router.register(r'showroom/detail', ShowroomDetailViewSet)

urlpatterns = [
    path("", include(router.urls))

]
