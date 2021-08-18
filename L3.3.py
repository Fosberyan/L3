def my_func(a, b, c):
    a = (a, b, c)
    a = sorted(a, reverse=True)

    return a[0] + a[1]


if __name__ == '__main__':
    result = my_func(30045, 10, 50040)

    print(f'Итого: {result}')