#!/usr/bin/python3
'''
Написать функцию, принимающую строку-пароль. Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. Условия:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре.
'''
import re


def check_passwd(t_string):
    """Функция, принимающая строку-пароль и проверяющая выполнение условий.
    """
    if (len(t_string) >= 6 and
            re.search('\d', t_string) != None and
            re.search('\D', t_string) != None and
            re.search('password', t_string.lower()) == None):
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_passwd(input('Введите пароль для проверки: ')))