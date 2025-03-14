"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*lst):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x**2 for x in lst]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if (x % i) == 0:
            return False
    return True


def filter_numbers(lst, flt):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if flt == EVEN:
        return list(filter(lambda x: x % 2 == 0, lst))
    elif flt == ODD:
        return list(filter(lambda x: x % 2 != 0, lst))
    return list(filter(is_prime, lst))


# print(power_numbers(1, 2, 5, 7))
# print(filter_numbers([1, 2, 3], ODD))
# print(filter_numbers([2, 3, 4, 5], PRIME))
