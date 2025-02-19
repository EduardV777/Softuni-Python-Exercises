from .hot_beverage import HotBeverage

class Coffee(HotBeverage):
    milliliters = 50
    price = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.price, self.milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine