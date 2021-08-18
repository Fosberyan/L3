import re
def divide_two_numbers(a, b):
    return a / b
if __name__ == '__main__':
    n_one = input('Что будем делить: ')
    n_two = input('на что будем делить: ')
    pattern = r'^\d+$'
    if not re.match(pattern, n_one) or not re.match(pattern, n_two):
        raise TypeError('Ошибка')
    result = None
    try:
        result = divide_two_numbers(int(n_one), int(n_two))
    except ZeroDivisionError:
        print('Деление на ноль')
        exit(1)
    print(f'Что то пошло не по плану: {result}')