numbers = [12, 45, 2, 89, 34, 6, 90, 23]

minimum = numbers[0]
maximum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

difference = maximum - minimum

print(f"Мінімум: {minimum}")
print(f"Максимум: {maximum}")
print(f"Різниця: {difference}")