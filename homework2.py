number = int(input("Введіть трицифрове число: "))

a = number // 100
b = (number // 10) % 10
c = number % 10

sum_squares = a**2 + b**2 + c**2

print(f"Сума квадратів цифр ({a}^2 + {b}^2 + {c}^2): {sum_squares}")