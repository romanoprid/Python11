from doctest import testmod
from typing import List

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.hockey_puck import HockeyPuck
from ua.lviv.iot.python.model.ice_skates import IceSkates
from ua.lviv.iot.python.model.level import Level
from ua.lviv.iot.python.model.protective_clothes import ProtectiveClothes
from ua.lviv.iot.python.model.purpose import Purpose
from ua.lviv.iot.python.model.uniform import Uniform


class ClubManager:
    # global doctest

    # def __init__(self):
    #     self.goods = list()
    #
    # def find_goods_for_some_purpose(self, purpose=Purpose.GOALKEEPER):
    #     """
    #         >>> manager = ClubManager(); manager.goods.append(HockeyPuck()); manager.goods.append(IceSkates())\
    #         ;manager.goods.append(ProtectiveClothes()); manager.goods.append(Uniform())\
    #         ;print(manager.find_goods_for_some_purpose(Purpose.GOALKEEPER))
    #         [HockeyPuck{name:HockeyPuck, price_in_ukrainian_hryvnas:200,\
    #         producer:North, producing country:UA}, Ice Skates{name:Ice Skates, price_in_ukrainian_hryvnas:200, producer:South, producing country:UK}, Protective Clothes{name:Protective Clothes, price_in_ukrainian_hryvnas:250, producer:North, producing country:USA}, Uniform{name:Uniform, price_in_ukrainian_hryvnas:130, producer:Lion, producing country:UA}]
    #         >>> print(manager.find_goods_for_some_purpose(Purpose.GOALKEEPER))
    #         [HockeyPuck{name:HockeyPuck, price_in_ukrainian_hryvnas:200, producer:North, producing country:UA}, Ice Skates{name:Ice Skates, price_in_ukrainian_hryvnas:200, producer:South, producing country:UK}, Protective Clothes{name:Protective Clothes, price_in_ukrainian_hryvnas:250, producer:North, producing country:USA}, Uniform{name:Uniform, price_in_ukrainian_hryvnas:130, producer:Lion, producing country:UA}]
    #     """
    #
    #     suitable = list()
    #     for good in self.goods:
    #         if good.purpose.__contains__(purpose):
    #             suitable.append(good)
    #     return suitable
    def __init__(self):
        self.list_of_goods: List[Good] = []

    def find_goods_by_name(self, name: str) -> List[Good]:
        """
        Test of correct founding goods by name in the list
        >>> club_manager = ClubManager()
        >>> club_manager.list_of_goods.append(HockeyPuck("HockeyPuck",200,"North","UA","Ruber",Purpose.GOALKEEPER,2))
        >>> club_manager.list_of_goods.append(HockeyPuck("HockeyPuck",150,"South","USA","Wood",Purpose.GOALKEEPER,2))
        >>> list_of_founded_goods_by_name = club_manager.find_goods_by_name("HockeyPuck")
        >>> len(list_of_founded_goods_by_name)
        2
        """
        list_of_founded_goods: List[Good] = []
        for good in self.list_of_goods:
            if good.name == name:
                list_of_founded_goods.append(good)
        return list_of_founded_goods

    def find_goods_by_producer(self, producer: str) -> List[Good]:
        """
        Test of correct founding goods by producer in the list
        >>> club_manager = ClubManager()
        >>> club_manager.list_of_goods.append(ProtectiveClothes("Coat",1500,"Lion","UK","Leather",Purpose.FIELDPLAYER,
        ... Level.HIGH))
        >>> club_manager.list_of_goods.append(IceSkates("Ice skates",300,"Grenland","UA","Leather",Purpose.FIELDPLAYER,
        ... 45))
        >>> list_of_founded_goods_by_producer = club_manager.find_goods_by_producer("Lion")
        """
        list_of_founded_goods: List[Good] = []
        for good in self.list_of_goods:
            if good.producer == producer:
                list_of_founded_goods.append(good)
        return list_of_founded_goods


if __name__ == '__main__':
    testmod(verbose=True)
