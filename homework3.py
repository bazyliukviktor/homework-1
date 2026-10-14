import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
expected_c = float(input("Введіть expected_c: "))

c = math.sqrt(a**2 + b**2)
perimeter = a + b + c

matches = abs(c - expected_c) <= 1e-6

print(f"Гіпотенуза: {c}, Периметр: {perimeter}, Збігається: {matches}")