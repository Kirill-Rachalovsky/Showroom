from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Showroom API')

urlpatterns = [
    path('swagger/', schema_view),
    path('dealer/', include('src.dealer.urls')),
    path('showroom/', include('src.showroom.urls')),
    path('customer/', include('src.customer.urls')),
    path('deals/', include('src.transactions.urls')),
]
