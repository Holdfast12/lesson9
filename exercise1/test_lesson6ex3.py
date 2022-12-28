#!/usr/bin/python3
import lesson6ex3


def test_xorfinc_hello_world_password():
    """Функция-тест для функции шифрования.
    В первой части условия проверяется шифрование и дешифрование с  одним и тем же паролем,
    во второй с разными паролями
    """
    assert (lesson6ex3.xorfunc(lesson6ex3.xorfunc('hello world', 'password'), 'password') == 'hello world' and
            lesson6ex3.xorfunc(lesson6ex3.xorfunc('hello world', 'password'), 'passphrase') != 'hello world')