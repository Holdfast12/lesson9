#!/usr/bin/python3
#Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.


def summ_parameters(*args):
    '''Функция, принимающая сколько угодно числовых и текстовых параметров
    (в том числе и 0) и возвращающая их суммы.
    '''
    t_numbers = 0
    t_strings = ''
    for i in args:
        if type(i) == int or type(i) == float:
            t_numbers += i
        elif type(i) == str:
            t_strings += i
    return t_numbers, t_strings


if __name__ == '__main__':
    parameters = input('Введите параметры через пробел, чтобы получить их сумму: ').split()
    for i in range(len(parameters)):
        try:
            parameters[i] = float(parameters[i]) if '.' in parameters[i] else int(parameters[i])
        except ValueError:
            print(f'Параметр {parameters[i]} будет принят как текстовый')

    summ_numbers, summ_strings = summ_parameters(*parameters)

    print(f'=======================================\n\
    Для введенных параметров\n\
    \tсумма чисел будет равна: {summ_numbers}\n\
    \tсумма строк будет такой: {summ_strings}')