from math import sqrt

# Задание 1(Определение високосного года):


def is_your_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


print(is_your_year(2000))

# Задание 2(Квадрат):


def square(x):
    p = 4 * x
    s = x * x
    d = x * sqrt(2)
    k = (p, s, d)
    return k


print(square(3))

# Задание 3(Время года):


def season(month):
    if 1 <= month <= 3:
        return 'Зима'
    elif 4 <= month <= 6:
        return 'Весна'
    elif 7 <= month <= 9:
        return 'Лето'
    elif 10 <= month <= 12:
        return 'Осень'
    else:
        return 'Некорректно введен месяц. Введите число от 1 до 12'


def get_season(month):
    seasons = {'Зима': (1, 2, 12),
              'Весна': (3, 4, 5),
              'Лето': (6, 7, 8),
              'Осень': (9, 10, 11)}
    for key in seasons.keys():
        if month in seasons[key]:
            return key


print(season(1))


# Задание 4(Вклад):

def bank(a, years):
    rate = 0.1
    summ = a * ((1 + rate) ** years)
    return round(summ, 2)


print(bank(1000, 10))


# Задание 5(Простое число):

def is_prime(number):
    if number > 1:
        i = 2
        while i <= sqrt(number):
            if number % i == 0:
                return ("Составное число")
            i += 1
        else:
            return ("Простое число")
    else:
        return ("Составное число")


print(is_prime(2))


# Задание 6(Календарь):


def date(d, m, y):
    # месяцы по 30 и 31 дню
    m30 = (4, 6, 9, 11)
    m31 = (1, 3, 5, 7, 8, 10, 12)
    x = 0
    # длина месяца
    if m in m30:
        x = 30
    elif m in m31:
        x = 31
    elif m == 2:
        x = 28
        # проверка на високосный год
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            x = 29
    # проверка наличия дня в месяце
    if 1 <= d <= x:
        return True
    else:
        return False


print(date(28, 2, 1990))


# Задание 7(арифметика):

def arithmetic(d, b, c):
    if c == '+':
        return d + b
    elif c == '-':
        return d - b
    elif c == '*':
        return d * b
    elif c == '/':
        return d / b


print(arithmetic(2, 3, '/'))


# Задание 8 (подсчет гласных):

def count_vowels(text):
    count = 0
    for letter in 'AEIOUaeiou':
        count += text.count(letter)
    return count


print(count_vowels('UAaiooigram'))


# Задание 9(развернуть строку):

def reverse_string(text):
    print(text[::-1])


reverse_string('gila')


# Задание 10(заглавные буквы каждого слова):

def capitalize_first(text):
    print(text.title())


capitalize_first('hello world')


# Задание 11(удаление повторяющихся символов):

def remove_duplicates(text):
    text_1 = []
    for c in text:
        if c not in text_1:
            text_1.append(c)
    text_2 = ''.join(text_1)
    return text_2

# Задание 12(Максимальное значение):


def find_maximum(numbers):
    print(max(numbers))


a = [1, 4, 2, 55, 42, 3, 11]


# Задание 13 (Убрать повторы):

def remove_duplicate(text):
    list_1 = set(text)
    list_2 = list(list_1)
    return list_2


text_s = ['a', 'aa', 'b', 'f', 'a', 'f']


# Задание 14 (развернуть список):

def reverse_list(text):
    text.reverse()
    return text


text_list = ['d', 'f', 'ff', 'dd']


# Задание 15:

def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


num = [1, 2, 5, 6]
print(calculate_average(num))


# Задание 16(Факториал):

def calculate_factorial(number):
    if number == 0:
        return 1
    for i in range(number):
        a = i * (number - 1)
        return a


# Задание 17:

nums = [3, 1, 2, 10, 1]


def ar(tet):
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums
