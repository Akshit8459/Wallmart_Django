from celery import shared_task
from .ai_module import update_product_prices

@shared_task
def periodic_price_update():
    update_product_prices()
