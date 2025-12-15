from testing.src.capitalize import capitalize


if capitalize('') != '':
    raise Exception('Функция работает неверно!')

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

print('Функция работает исправно.')
