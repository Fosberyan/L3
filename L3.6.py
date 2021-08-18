def uppercase_first_char(string):
    x = str(string).split(' ')
    x = filter(lambda w: bool(w), x)
    x = map(lambda w: str(w[0]).upper() + str(w[1::]), x)
    return ' '.join(x)
if __name__ == '__main__':
    input_string = input('Два слова через пробел: ')
    modified_string = uppercase_first_char(input_string)
    print(f'Result: {modified_string}')