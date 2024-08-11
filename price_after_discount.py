def calculate_discounted_price(price: int | float, discount: int | float) -> int:
    if price < 0:
        raise ValueError()
    if discount < 0 or discount > 100:
        raise ValueError()
    result = price * (1 - discount / 100)
    return int(result)


