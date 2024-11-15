# 1st program
# Задача 1 "Арифметика"
result1 = 9 ** 0.5 * 5
print(result1)  # Ожидаемый результат: 15.0

# 2nd program
# Задача 2 "Логика"
result2 = (9.99 > 9.98) and (1000 != 1000.1)
print(result2)  # Ожидаемый результат: True

# 3rd program
# Задача 3 "Школьная загадка"
result3_no_priority = 2 * 2 + 2  # Без приоритета
result3_with_priority = 2 * (2 + 2)  # С приоритетом
result3_comparison = result3_no_priority == result3_with_priority
print(result3_no_priority)  # Ожидаемый результат: 6
print(result3_with_priority)  # Ожидаемый результат: 8
print(result3_comparison)  # Ожидаемый результат: False

# 4th program
# Задача 4 "Первый после точки"
number_str = '123.456'
number_float = float(number_str)  # Преобразование строки в дробное число
first_digit_after_decimal = int((number_float * 10) % 10)  # Умножаем на 10 и берем остаток от деления на 10
print(first_digit_after_decimal)  # Ожидаемый результат: 4

