# tests/test_calculadora.py

import pytest
from src.calculadora import suma, resta, multiplica, divide

def test_suma():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(10, 20) == -10

def test_multiplica():
    assert multiplica(4, 3) == 12
    assert multiplica(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

    with pytest.raises(ValueError):  # Verifica que se levante un error al dividir por cero
        divide(5, 0)
