"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

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

def test_name_setter():
    """
    Тестируем сеттер для name.
    """
    item = Item('Телефон', 10000, 5)
    item.name = 'Нов тел'
    assert item.name == 'Нов тел'

def test_instantiate_from_csv():
    """Test classmethod"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    """Test staticmethod"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    """Test __repr__"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("IPhone", 50, 300)
    item3 = Item("Nokia", 20000, 1)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('IPhone', 50, 300)"
    assert repr(item3) == "Item('Nokia', 20000, 1)"

def test_str():
    """Test __str__"""
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'IPhone'
    assert str(item3) == 'Nokia'


phone1 = Phone("iPhone 14", 120_000, 5, 2)
def test_Phone_init():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

def test_add():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
