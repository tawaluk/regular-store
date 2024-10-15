"""Дескрипторы для сущностей"""


class Descriptor:

    def __init__(self, name, value=None) -> None:
        self.name = name
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        return self.value


class NumberDescriptor(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Number must be an integer.")
        super().__set__(instance, value)


class StringDescriptor(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Must be a string.")
        super().__set__(instance, value)


class PriceDescriptor(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Price must be a float or an integer.")
        super().__set__(instance, float(value))


class IntDescriptor(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Amount must be an integer.")
        super().__set__(instance, value)
