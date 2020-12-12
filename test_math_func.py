import math_func
import pytest


@pytest.mark.parametrize('math_add',
                         [[math_func.add(7, 3),10],
                          [math_func.add(7),9],
                          [math_func.add(-7, -3),-10],
                          [math_func.add(-7, 3),-4],
                          [math_func.add(7.3, 3.3),10.6],
                          [math_func.add(7, -3),4],
                          [math_func.add(7.3, 3),10.3],
                          [math_func.add(7, 3.4),10.4],
                          ])
def test_add_2(math_add):
    math_adds = math_add
    assert math_adds[0] ==math_adds[1]

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9


def test_multiply():
    assert math_func.multiply(7, 3) == 21
    assert math_func.multiply(7) == 14


def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36


def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result
    print('--------------', math_func.add('Hello ', 'World'), '--------------')


def test_multiply_strings():
    assert math_func.multiply('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.multiply('Hello ')
    assert  result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
