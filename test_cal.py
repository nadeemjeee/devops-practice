import pytest
from cal import Calculator

@pytest.fixture
def cal():
    return Calculator()

def test_add(cal):
    assert cal.add(2,3)==5

def test_substract(cal):
    assert cal.substract(9,5)==4

def test_multiply(cal):
    assert cal.multiply(9,5)==45
