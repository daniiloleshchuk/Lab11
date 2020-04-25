from abc import ABC


class AbstractProduct(ABC):

    def __init__(self, type_of_product: str, color: str, height_in_sm: int, price_in_uah):
        self.type_of_product = type_of_product
        self.color = color
        self.height_in_sm = height_in_sm
        self.price_in_uah = price_in_uah
