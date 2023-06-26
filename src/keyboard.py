from src.item import Item


class Mixin:

    def __init__(self):
        self.__language = 'EN'

    def __str__(self):
        return self.__language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self

class Keyboard(Item, Mixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name




