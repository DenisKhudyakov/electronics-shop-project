"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.mark.parametrize("name, price, quantity, result", [("Смартфон", 10000, 20, 10000)])
def test_class(name, price, quantity, result):
    assert Item(name, price, quantity).apply_discount() == result