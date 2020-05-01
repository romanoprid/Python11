from abc import ABC

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.purpose import Purpose


class HockeyPuck(Good, ABC):
    # def __init__(self, name="HockeyPuck", price_in_ukrainian_hryvnas=200, producer="North",
    #              producing_country="UA", purpose=None, radius=2):
    #     self.radius = radius
    #     if purpose is None:
    #         purpose = list()
    #         purpose.append(Purpose.GOALKEEPER)
    #         purpose.append(Purpose.GOALKEEPER)
    #     super(HockeyPuck, self).__init__(name=name, price_in_ukrainian_hryvnas=price_in_ukrainian_hryvnas,
    #                                      producer=producer, producing_country=producing_country, purpose=purpose)
    #
    # def __str__(self):
    #     return "HockeyPuck{" + super(HockeyPuck, self).__str__() + "}"
    #
    # def __repr__(self):
    #     return "HockeyPuck{" + super(HockeyPuck, self).__repr__() + "}"

    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount,
                 purpose: Purpose, radius: float) -> None:
        Good.__init__(self, name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose)
        self.radius = radius
