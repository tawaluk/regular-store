"""Протоколы и тп."""

from typing import Protocol

from src.main_app.domain.entity import Product


class ProductRepo(Protocol):
    """Интерфейс для получения товара."""

    def get_by_article(self, article: int) -> Product:
        ...


class ProductsRepo(Protocol):
    """Интерфейс для получения товаров."""

    def get_list_by_category(self, category: str) -> list[Product]:
        ...
