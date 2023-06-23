import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> str:
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception ("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item из csv файла.
        """
        Item.all = []
        filename = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(filename, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Преобразует строку в число.
        """
        return int(float(string))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.quantity + other.quantity





