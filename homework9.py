def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Відсоток знижки має бути від 0 до 100")

    return price * (1 - discount_percent / 100)


assert calculate_discount(200.0, 15.0) == 170.0

assert calculate_discount(100.0, 0.0) == 100.0
assert calculate_discount(100.0, 50.0) == 50.0
assert calculate_discount(100.0, 100.0) == 0.0
assert calculate_discount(50.0, 10.0) == 45.0

try:
    calculate_discount(-100.0, 10.0)
    assert False
except ValueError:
    pass

try:
    calculate_discount(100.0, -5.0)
    assert False
except ValueError:
    pass

try:
    calculate_discount(100.0, 105.0)
    assert False
except ValueError:
    pass

print("Автотести пройшли успішно")