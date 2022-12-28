#!/usr/bin/python3
import lesson6ex2


def test_calc_cho_60_60_60():
    """Функция-тест для функции получения максимально возможного количества молекул C H O.
    """
    assert lesson6ex2.calc_cho(60, 60, 60) == 10