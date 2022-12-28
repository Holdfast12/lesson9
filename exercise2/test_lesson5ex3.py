#!/usr/bin/python3
import lesson5ex3


def test_fibonacci_10():
    """Проверка числа Фибоначчи под номером 10"""
    assert lesson5ex3.fibonacci(10) == 55


def test_fibonacci_0():
    """Проверка числа Фибоначчи под номером 0"""
    assert lesson5ex3.fibonacci(0) == 0