"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("IPhone", 50, 300)
item3 = Item("Nokia", 20000, 1)
def test_init():
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_calculate_total_price():

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 15000
    assert item3.calculate_total_price() == 20000

def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 10000

    Item.pay_rate = 0.8
    item2.apply_discount()
    assert item2.price == 40

    Item.pay_rate = 1.5
    item3.apply_discount()
    assert item3.price == 30000