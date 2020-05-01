from abc import ABC

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.purpose import Purpose
from ua.lviv.iot.python.model.size import Size


class Uniform(Good, ABC):
    # def __init__(self, name="Uniform", price_in_ukrainian_hryvnas=130, producer="Lion", producing_country="UA",
    #              purpose=None, size=None):
    #     if purpose is None:
    #         purpose = list()
    #         purpose.append(Purpose.GOALKEEPER)
    #         purpose.append(Purpose.GOALKEEPER)
    #     if size is None:
    #         size = list()
    #         size.append(Size.L)
    #         size.append(Size.S)
    #     super(Uniform, self).__init__(name=name, price_in_ukrainian_hryvnas=price_in_ukrainian_hryvnas,
    #                                   producer=producer, producing_country=producing_country,
    #                                   purpose=purpose)
    #
    # def __str__(self):
    #     return "Uniform{" + super(Uniform, self).__str__() + "}"
    #
    # def __repr__(self):
    #     return "Uniform{" + super(Uniform, self).__repr__() + "}"
    def __init__(self, name: str, price_in_ukrainian_hryvnas: float, producer: str, producing_country: str,
                 material: str, amount,
                 purpose: Purpose, size: Size) -> None:
        Good.__init__(self, name, price_in_ukrainian_hryvnas, producer, producing_country, material, amount, purpose)
        self.size = size
