import random

def dynamic_price_adjustment(product, competitor_prices, demand_forecast):
    new_price = product.current_price

    # Adjust based on competitor prices
    competitor_average = sum([cp.price for cp in competitor_prices]) / len(competitor_prices)
    new_price = (new_price + competitor_average) / 2

    # Adjust based on demand forecast
    if demand_forecast.predicted_demand > 100:
        new_price *= 1.1  # Increase price if demand is high
    elif demand_forecast.predicted_demand < 50:
        new_price *= 0.9  # Decrease price if demand is low

    return new_price

def update_product_prices():
    from .models import Product, CompetitorPrice, DemandForecast, PriceHistory
    
    products = Product.objects.all()

    for product in products:
        competitor_prices = CompetitorPrice.objects.filter(product=product)
        demand_forecast = DemandForecast.objects.filter(product=product).order_by('-forecast_date').first()
        
        if competitor_prices and demand_forecast:
            new_price = dynamic_price_adjustment(product, competitor_prices, demand_forecast)
            product.current_price = new_price
            product.save()

            # Log price change
            PriceHistory.objects.create(product=product, price=new_price)
