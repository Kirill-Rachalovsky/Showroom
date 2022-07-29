from django.urls import path, include
from rest_framework import routers
from src.showroom.views import *

router = routers.DefaultRouter()
router.register(r'list', ShowroomViewSet)
router.register(r'detail', ShowroomDetailViewSet)

urlpatterns = [
    path("", include(router.urls))
]
