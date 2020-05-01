from abc import ABC

from ua.lviv.iot.python.model.purpose import Purpose


class Good(ABC):
    # def __init__(self, name="Bit", price_in_ukrainian_hryvnas=200, producer="North", producing_country="UA",
    #              purpose=None):
    #     if purpose is None:
    #         purpose = list()
    #     self.name = name
    #     self.price_in_ukrainian_hryvnas = price_in_ukrainian_hryvnas
    #     self.producer = producer
    #     self.producing_country = producing_country
    #     self.purpose = purpose
    #
    # def __del__(self):
    #     return
    #
    # def __str__(self):
    #     return "name:" + self.name + ", price_in_ukrainian_hryvnas:" + str(self.price_in_ukrainian_hryvnas) + \
    #            ", producer:" + str(self.producer) \
    #            + ", producing country:" + str(self.producing_country)
    #
    # def __repr__(self):
    #     return "name:" + self.name + ", price_in_ukrainian_hryvnas:" + str(self.price_in_ukrainian_hryvnas) + \
    #            ", producer:" + str(self.producer) \
    #            + ", producing country:" + str(self.producing_country)
    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount: float,
                 purpose: Purpose) -> None:
        self.name = name
        self.price_in_ukrainian_hryvnas = price_in_ukrainian_hryvnas
        self.producer = producer
        self.producing_country = producing_country
        self.material = material
        self.country_code = amount
        self.purpose = purpose
