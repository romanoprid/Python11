from abc import ABC

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.level import Level
from ua.lviv.iot.python.model.purpose import Purpose


class ProtectiveClothes(Good, ABC):
    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount,
                 purpose: Purpose, protection_level:Level) -> None:
        Good.__init__(self, name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose)
        self.protection_level = protection_level