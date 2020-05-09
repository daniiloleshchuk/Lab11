from abc import ABC


class AbstractProduct():

    def __init__(self, type_of_product: str, color: str, height_in_sm: int, price_in_uah):
        self.type_of_product = type_of_product
        self.color = color
        self.height_in_sm = height_in_sm
        self.price_in_uah = price_in_uah

    def __str__(self):
        return "Type of product is: " + str(self.type_of_product) + "\n" \
                                                                    "Color is: " + str(self.color) + "\n" \
                                                                                                     "Height in sm is: " + str(
            self.height_in_sm) + "\n" \
                                 "Price in UAH is: " + str(self.price_in_uah) + "\n"
