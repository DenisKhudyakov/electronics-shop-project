"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.mark.parametrize("name, price, quantity, result", [("Смартфон", 10000, 20, 200000)])
def test_calculate_total_price(name, price, quantity, result):
    assert Item(name, price, quantity).calculate_total_price() == result



@pytest.mark.parametrize('price, discount, price_with_discount', [(10_000, 0, 10_000),
        (10_000, 0.15, 8_500),
        (10_000, 0.27, 7_300)])
def test_apply_discount(price, discount, price_with_discount):
    test_item = Item('Машинка', price=price, quantity=10)
    test_item.pay_rate = 1 - discount
    assert test_item.apply_discount() == price_with_discount



