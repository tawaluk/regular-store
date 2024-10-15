"""Шаблоны юзкейсов"""

from main_app.app.actions import StandardСostProduct, StandartСostOrder
from main_app.app.entity import ProductRepo
from main_app.domain.entity import Order, Product


class PresentProduct:
    """Подготовка продукта к виду, нужному для продажи"""

    def __init__(
        self, product: ProductRepo, price: StandardСostProduct
    ) -> None:
        self._product = product
        self._price = price

    def __call__(
        self, article, tax: int, discount: int, margin: int
    ) -> Product:

        product = self._product(article)
        price = self._price(product, tax, discount, margin)
        product.final_price = product.amount * price

        return product


class PresentOrder:
    """Подготовка заказа к виду, нужному для продажи"""

    def __init__(
        self, order: Order, price: StandartСostOrder
    ) -> None:
        self.order = order
        self._price = price

    def __call__(self, order, factor: int) -> Order:

        order = self.order
        price = self._price(order, factor)
        order.total_final_price = order.base_total_price * price

        return order
