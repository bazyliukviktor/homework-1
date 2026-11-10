import time

n = 500_000

# Створюємо список і множину
numbers_list = list(range(n))
numbers_set = set(numbers_list)

target = 499_999

# Пошук у списку
start_list = time.perf_counter()
target in numbers_list
end_list = time.perf_counter()

list_time = end_list - start_list

# Пошук у множині
start_set = time.perf_counter()
target in numbers_set
end_set = time.perf_counter()

set_time = end_set - start_set

print(f"List search: {list_time:.6f} сек")
print(f"Set search: {set_time:.6f} сек")