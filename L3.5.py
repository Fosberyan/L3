import re
t = 0
e = False
while not e:
    n_str = input('Программа запрашивает у пользователя строку чисел, разделенных пробелом или конец: ')
    n = n_str.split(' ')
    n = map(lambda n: str(n).strip(), n)
    n = filter(lambda n: bool(n), n)
    pattern = r'^\d+$'
    for num in n:
        if num == 'Конец':
            e = True
            break
        if not re.match(pattern, num):
            raise ValueError(f'Неверныйномер {num}.')
        t += int(num)
    print(f'Итог: {t}')