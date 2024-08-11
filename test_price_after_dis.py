from price_after_discount import calculate_discounted_price


def test_discount_no_discount():
    price = 100
    discount = 0
    expected = 100
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected


def test_discount_full_discount():
    price = 100
    discount = 100
    expected = 0
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected


def test_discount_half_discount():
    price = 100
    discount = 50
    expected = 50
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected


def test_no_discount_for_zero_price():
    price = 0
    discount = 0
    expected = 0
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected


def test_small_discount():
    price = 200
    discount = 10
    expected = 180
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected
