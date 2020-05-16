from models.AbstractProduct import AbstractProduct


class Flower(AbstractProduct):
    def __init__(self, type_of_product: str, color: str, height_in_sm: int, price_in_uah: int, type_of_flower: str):
        super().__init__(type_of_product, color, height_in_sm, price_in_uah)
        self.type_of_flower = type_of_flower

    def __str__(self):
        return super.__str__(self) + \
               "Type of flower is: " + str(self.type_of_flower) + "\n"
