import re
def exponentiation(number, exp):

    if exp < 1:
        raise ValueError('...')
    itog = number
    for _ in range(1, exp):
        itog = itog * number
    return itog

if __name__ == '__main__':
    number = input('Число: ')
    exponent = input('Степень: ')
    pattern = r'^\d+$'

    if not re.match(pattern, number) or not re.match(pattern, exponent):
        raise TypeError('Only digits allowed.')
    itog = exponentiation(int(number), int(exponent))
    print(f'Итого: {itog}')