import time
import random


def run_with_information(fn, *args, **kwargs):
    t1 = time.time()
    print('Начало выполнения:')
    print(t1)
    print('Неименованные аргументы: {}'.format(args))
    print('Именованные аргументы: {}'.format(kwargs))
    result = fn(*args, **kwargs)
    t2 = time.time()
    print('Окончание выполнения:')
    print(t2)
    print('Результат: {}'.format(result))
    print('Время выполнения (сек):')
    print(t2 - t1)
    return result


def sleep_function(t=random.randint(1, 5)):
    time.sleep(t)
    return t

delay = input('Введите число (пустая строка = случайный параметр): ')
if delay == '':
    run_with_information(sleep_function)
else:
    try:
        delay = int(delay)
        run_with_information(sleep_function, delay)
    except ValueError:
        print('Ошибка ввода данных')

