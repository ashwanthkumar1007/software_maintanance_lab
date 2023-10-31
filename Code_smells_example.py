def calculate_total_price(items):
    total = 0
    for item in items:
        total += calculate_item_price(item)
    return total

def calculate_item_price(item):
    price = item.price
    if item.quantity > 0:
        price *= 0.9 if price > 100 else 0.95
    return price
