from models.AbstractProduct import AbstractProduct


class Vase(AbstractProduct):
    def __init__(self, type_of_product: str, color: str, height_in_sm: int, price_in_uah, volume_in_ml):
        super().__init__(type_of_product, color, height_in_sm, price_in_uah)
        self.volume_in_ml = volume_in_ml

    def __str__(self):
        return super.__str__(self) + \
               "Volume in ml is: " + str(self.volume_in_ml) + "\n"
