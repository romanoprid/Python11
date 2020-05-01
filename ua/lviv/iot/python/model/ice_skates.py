from abc import ABC

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.purpose import Purpose


class IceSkates(Good, ABC):
    # def __init__(self, name="Ice Skates", price_in_ukrainian_hryvnas=200, producer="South",
    #              producing_country="UK", purpose=None, foot_size=45):
    #     self.foot_size = foot_size
    #     if purpose is None:
    #         purpose = list()
    #         purpose.append(Purpose.GOALKEEPER)
    #         purpose.append(Purpose.GOALKEEPER)
    #     super(IceSkates, self).__init__(name=name, price_in_ukrainian_hryvnas=price_in_ukrainian_hryvnas,
    #                                     producer=producer, producing_country=producing_country,
    #                                     purpose=purpose)
    #
    # def __str__(self):
    #     return "Ice Skates{" + super(IceSkates, self).__str__() + "}"
    #
    # def __repr__(self):
    #     return "Ice Skates{" + super(IceSkates, self).__repr__() + "}"
    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount,
                 purpose: Purpose, foot_size: float) -> None:
        Good.__init__(self, name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose)
        self.foot_size = foot_size
