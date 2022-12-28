#!/usr/bin/python3
import lesson5ex2


def test_summ_parameters_76_7_2_6p6_hdf_ew():
    """Проверка функции summ_parameters() с числами и строками в качестве параметров"""
    assert lesson5ex2.summ_parameters(76, 7, 2, 6.6, 'hdf', 'ew') == (91.6, 'hdfew')


def test_summ_parameters_32_64_412():
    """Проверка функции summ_parameters() с числами в качестве параметров"""
    assert lesson5ex2.summ_parameters(32, 64, 412) == (508, '')


def test_test_summ_parameters_dfhdf_ghqw_gjh():
    """Проверка функции summ_parameters() со строками в качестве параметров"""
    assert lesson5ex2.summ_parameters('dfhdf', 'ghqw', 'gjh') == (0, 'dfhdfghqwgjh')


def test_test_summ_parameters():
    """Проверка функции summ_parameters() без параметров"""
    assert lesson5ex2.summ_parameters() == (0, '')