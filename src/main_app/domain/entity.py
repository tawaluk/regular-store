"""Корневые сущности"""

from datetime import datetime

from .descriptors import (
    Descriptor, NumberDescriptor, StringDescriptor
)


class Product:

    def __init__(
            self,
            article: int,
            name: str,
            description: str,
            base_price: int,  # себестоимость
            amount: int,
            category: str
    ) -> None:
        self.article = article
        self.name = name
        self.description = description
        self.base_price = base_price
        self.amount = amount
        self.category = category

    def __str__(self) -> str:
        return (
            f"Product: article - {self.article}, name - {self.name},"
            f"description - {self.description},"
            f"base_price - {self.base_price},"
            f"amount - {self.amount},"
            f"category - {self.category}"
        )


class Order:

    number = NumberDescriptor("number")
    name = StringDescriptor("name")
    comment = StringDescriptor("comment")
    status = StringDescriptor("status")
    create_date = Descriptor("create_date")
    completion_date = Descriptor("completion_date")

    def __init__(
            self,
            number: int,
            name: str,
            comment: str,
            status: str,
            create_date: datetime | None = None,
            completion_date: datetime | None = None,
            products: list[Product] = None,
    ) -> None:
        self.number = number
        self.name = name
        self.comment = comment
        self.status = status
        self.create_date = create_date if create_date else datetime.now()
        self.completion_date = completion_date
        self.products = products if products is not None else []

    @property
    def base_total_price(self) -> int:
        """
        Расчет базовой стоимости. Тут не учитывается ничего из скидок и тп.
        """

        return sum(
            product.base_price * product.amount for product in self.products
        )

    def __str__(self) -> str:
        products_str = ', '.join(str(product) for product in self.products)

        return (
            f"Order: number - {self.number}, name - {self.name},"
            f"comment - {self.comment}, status - {self.status},"
            f"create_date - {self.create_date},"
            f"completion_date - {self.completion_date},"
            f"base_total_price - {self.base_total_price},"
            f"Products - [{products_str}]."
        )
