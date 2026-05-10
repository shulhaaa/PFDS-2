import numpy as np

# Створення масиву з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

# Маска для додатних чисел
positive_mask = arr > 0
positive_numbers = arr[positive_mask]

print("\nДодатні числа:")
print(positive_numbers)

# Замінюємо всі від’ємні значення на нулі
arr[arr < 0] = 0

print("\nМасив після заміни від’ємних чисел на 0:")
print(arr)

# Обчислення середнього значення
average = np.mean(arr)

print("\nСереднє значення масиву:", average)