import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     "add-cars-every-three-minutes": {
#         "task": "src.car.tasks.car_task",
#         "schedule": crontab(minute="*/3"),
#     },
#     "buy-showroom-shipper-every-single-minute": {
#         "task": "src.showroom.tasks.dealer_showroom_offer",
#         "schedule": crontab(minute="*/1"),
#     },
#     "showroom-make-discount-car": {
#         "task": "src.showroom.tasks.add_cars_discounts",
#         "schedule": crontab(minute="*/3"),
#     },
#     "buy-customer-showroom-every-two-minutes": {
#         "task": "src.customer.tasks.make_customer_offer",
#         "schedule": crontab(minute="*/2"),
#     },
# }
