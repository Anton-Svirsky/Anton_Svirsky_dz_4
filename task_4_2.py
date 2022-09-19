""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.  """


def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def func_search(num):
    rezult = []
    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult


num = input_numbers("Введите натуральное число N: ")
print(func_search(num))

