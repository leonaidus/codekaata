from typing import List, Tuple

from Product import Product


class Cart:

    def __init__(self):
        self.products_quantity_map: List[Tuple[Product, int]] = []

    @property
    def _prices_and_total(self) -> (List[float], float):
        _prices: List[float] = []
        total: float = 0.0
        for product, quantity in self.products_quantity_map:
            if product.offer is not None:
                discounted_sets = quantity // product.offer.quantity
                remaining_items = quantity % product.offer.quantity
                product_total = discounted_sets * product.offer.price + remaining_items * product.price
            else:
                product_total = product.price * quantity
            _prices.append(product_total)
            total += product_total
        return _prices, total

    @property
    def total(self) -> float:
        _, total = self._prices_and_total
        return total

    def _find_product_from_name(self, name: str) -> Tuple[Tuple[Product, int] or None, int]:
        for idx, (_product, _quantity) in enumerate(self.products_quantity_map):
            if _product.name == name:
                return (_product, _quantity), idx
        return (None, None), -1

    def add(self, name: str):
        (_product, _quantity), idx = self._find_product_from_name(name)
        if idx == -1:
            product = Product(name)
            self.products_quantity_map.append((product, 1))
        else:
            self.products_quantity_map[idx] = (_product, _quantity + 1)
