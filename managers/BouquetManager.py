from models.Flower import Flower


class BouquetManager:

    def __init__(self):
        self.flowers_in_bouquet = []

    def add_flowers_to_bouquet(self, *flowers_to_add: Flower):
        for flower in flowers_to_add:
            self.flowers_in_bouquet.append(flower)

    def remove_flowers_from_bouquet(self, *flowers_to_remove: Flower):
        for flower in flowers_to_remove:
            self.flowers_in_bouquet.remove(flower)

    def find_flower_price_lower_than(self, price_to_compare: int):
        """
        >>> rose = Flower("flower", "red", 40, 70, "rose")
        >>> fialka = Flower("flower", "purple", 20, 35, "fialka")
        >>> romashka = Flower("flower", "white", 10, 20, "romashka")
        >>> bouquet = BouquetManager()
        >>> bouquet.add_flowers_to_bouquet(rose, fialka, romashka)
        >>> result = bouquet.find_flower_price_lower_than(60)
        >>> [flower.price_in_uah for flower in result]
        [35, 20]
        """
        result: list = []
        for flower in self.flowers_in_bouquet:
            if flower.price_in_uah < price_to_compare:
                result.append(flower)
        return result

    def find_flowers_height_bigger_than(self, height_in_sm_to_compare: int):
        """
        >>> rose = Flower("flower", "red", 40, 70, "rose")
        >>> fialka = Flower("flower", "purple", 20, 35, "fialka")
        >>> romashka = Flower("flower", "white", 10, 20, "romashka")
        >>> bouquet = BouquetManager()
        >>> bouquet.add_flowers_to_bouquet(rose, fialka, romashka)
        >>> result = bouquet.find_flowers_height_bigger_than(15)
        >>> [flower.height_in_sm for flower in result]
        [40, 20]
        """
        result: list = []
        for flower in self.flowers_in_bouquet:
            if flower.height_in_sm > height_in_sm_to_compare:
                result.append(flower)
        return result

    def sort_flowers_by_height(self, reverse=True):
        """
        >>> rose = Flower("flower", "red", 40, 70, "rose")
        >>> fialka = Flower("flower", "purple", 20, 35, "fialka")
        >>> romashka = Flower("flower", "white", 10, 20, "romashka")
        >>> bouquet = BouquetManager()
        >>> bouquet.add_flowers_to_bouquet(rose, fialka, romashka)
        >>> bouquet.sort_flowers_by_height(reverse=False)
        >>> [flower.height_in_sm for flower in bouquet.flowers_in_bouquet]
        [10, 20, 40]
        >>> bouquet.sort_flowers_by_height(reverse=True)
        >>> [flower.height_in_sm for flower in bouquet.flowers_in_bouquet]
        [40, 20, 10]
        """
        self.flowers_in_bouquet.sort(key=lambda flower: flower.height_in_sm, reverse=reverse)

    def sort_flowers_by_price(self, reverse=False):
        """
        >>> rose = Flower("flower", "red", 40, 70, "rose")
        >>> fialka = Flower("flower", "purple", 20, 35, "fialka")
        >>> romashka = Flower("flower", "white", 10, 20, "romashka")
        >>> bouquet = BouquetManager()
        >>> bouquet.add_flowers_to_bouquet(rose, fialka, romashka)
        >>> bouquet.sort_flowers_by_price()
        >>> [flower.price_in_uah for flower in bouquet.flowers_in_bouquet]
        [20, 35, 70]
        >>> bouquet.sort_flowers_by_price(reverse=True)
        >>> [flower.price_in_uah for flower in bouquet.flowers_in_bouquet]
        [70, 35, 20]
        """
        self.flowers_in_bouquet.sort(key=lambda flower: flower.price_in_uah, reverse=reverse)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=False, extraglobs={'bouquet': BouquetManager()})
