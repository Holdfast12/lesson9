#!/usr/bin/python3
import lesson5ex1


def test_check_passwd_123456():
    """Проверка функции check_passwd() паролем из одних лишь цифр"""
    assert lesson5ex1.check_passwd('123456') == False


def test_check_passwd_asddfhj7():
    """Проверка функции check_passwd() хорошим паролем"""
    assert lesson5ex1.check_passwd('asddfhj7') == True


def test_check_passwd_hdfhhjfjh():
    """Проверка функции check_passwd() паролем без цифр"""
    assert lesson5ex1.check_passwd('hdfhhjfjh') == False


def test_check_passwd_hdfh2():
    """Проверка функции check_passwd() слишком коротким паролем"""
    assert lesson5ex1.check_passwd('hdfh2') == False


def test_check_passwd_hdfh2():
    """Проверка функции check_passwd() паролем со словом 'password'"""
    assert lesson5ex1.check_passwd('password123') == False