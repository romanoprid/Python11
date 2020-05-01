from abc import ABC

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.level import Level
from ua.lviv.iot.python.model.purpose import Purpose


class ProtectiveClothes(Good, ABC):
    # def __init__(self, name="Protective Clothes", price_in_ukrainian_hryvnas=250, producer="North",
    #              producing_country="USA", purpose=None, protection_level=None):
    #     self.protection_level = protection_level
    #     if purpose is None:
    #         purpose = list()
    #         purpose.append(Purpose.GOALKEEPER)
    #         purpose.append(Purpose.GOALKEEPER)
    #     if protection_level is None:
    #         protection_level = list()
    #         protection_level.append(Purpose.GOALKEEPER)
    #         protection_level.append(Purpose.GOALKEEPER)
    #     super(ProtectiveClothes, self).__init__(name=name, price_in_ukrainian_hryvnas=price_in_ukrainian_hryvnas,
    #                                             producer=producer, producing_country=producing_country,
    #                                             purpose=purpose)
    #
    # def __str__(self):
    #     return "Protective Clothes{" + super(ProtectiveClothes, self).__str__() + "}"
    #
    # def __repr__(self):
    #     return "Protective Clothes{" + super(ProtectiveClothes, self).__repr__() + "}"
    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount,
                 purpose: Purpose, protection_level:Level) -> None:
        Good.__init__(self, name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose)
        self.protection_level = protection_level