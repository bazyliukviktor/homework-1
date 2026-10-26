n = 30
sum_primes = 0
prime_numbers = []

for num in range(2, n + 1):
    is_prime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        sum_primes += num
        prime_numbers.append(num)

print(f"Сума простих чисел від 2 до {n} ({'+'.join(map(str, prime_numbers))}): {sum_primes}")