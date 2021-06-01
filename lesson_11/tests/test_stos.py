import pytest
from main import Stos


def test_create_stos():
    stos = Stos(5)
    assert stos.maxsize == 5
    assert stos.arr == []
    assert isinstance(stos, Stos)


def test_add_item_stos():
    stos = Stos(5)

    stos.push(100)

    assert stos.size() == 1
    assert stos.size() < 5


def test_add_two_items_stos():
    stos = Stos(2)

    stos.push(1)
    stos.push(-123)

    assert stos.size() == 2
    assert stos.size() == stos.maxsize


def test_pop_item_stos():
    stos = Stos(2)
    stos.push(1)

    stos.pop()

    assert stos.size() == 0


def test_pop_two_items_stos():
    stos = Stos(2)
    stos.push(1)
    stos.push(2)

    stos.pop()
    stos.pop()

    assert stos.size() == 0


def test_top_stos():
    stos = Stos(3)
    stos.push(123)
    stos.push(32)

    assert stos.top() == 32


def test_size_stos():
    stos = Stos(2)
    stos.push(1)
    stos.push(2)
    stos.pop()

    assert stos.size() == 1


def test_full_stos():
    stos = Stos(2)
    stos.push(1)
    stos.push(2)
    assert stos.full()


def test_empty_stos():
    stos = Stos(2)
    stos.push(2)
    stos.pop()

    assert stos.empty()