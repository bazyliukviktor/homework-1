def digital_root(n):
    # Якщо число однозначне то повертаємо його
    if n < 10:
        return n

    # Сума цифр числа
    digit_sum = sum(int(digit) for digit in str(n))

    # Рекурсивний виклик
    return digital_root(digit_sum)


number = 9875

result = digital_root(number)

print("Цифровий корінь:", result)