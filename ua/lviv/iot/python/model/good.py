from abc import ABC

from ua.lviv.iot.python.model.purpose import Purpose


class Good(ABC):

    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount: float,
                 purpose: Purpose) -> None:
        self.name = name
        self.price_in_ukrainian_hryvnas = price_in_ukrainian_hryvnas
        self.producer = producer
        self.producing_country = producing_country
        self.material = material
        self.amount = amount
        self.purpose = purpose
