"""Стратегии"""


from typing import Protocol


class StandardСostProduct(Protocol):
    """Обычная модель расчета стоимости товара"""

    def calculate_cost(
            self, base_cost: int, tax: int, discount: int, margin: int
    ) -> int:
        """Расчет стоимости товара"""
        ...


class StandartСostOrder(Protocol):
    """Обычная модель расчета стоимости заказа"""

    def calculate_cost(self, base_cost: int, factor: int) -> int:
        """Расчет стоимости заказа"""
        ...
