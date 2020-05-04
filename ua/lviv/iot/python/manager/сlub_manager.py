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

    def __init__(self):
        self.list_of_goods: List[Good] = []

    def find_goods_by_name(self, name: str) -> List[Good]:
        """
        Test of correct founding goods by name in the list
        >>> club_manager = ClubManager()
        >>> club_manager.list_of_goods.append(HockeyPuck("HockeyPuck",200,"North","UA","Ruber",245,Purpose.GOALKEEPER,
        ... 2))
        >>> club_manager.list_of_goods.append(HockeyPuck("HockeyPuck",150,"South","USA","Wood",3450,Purpose.GOALKEEPER,
        ... 2))
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
        >>> club_manager.list_of_goods.append(ProtectiveClothes("Coat",1500,"Lion","UK","Leather",2000,
        ... Purpose.FIELDPLAYER, Level.HIGH))
        >>> club_manager.list_of_goods.append(IceSkates("Ice skates",300,"Grenland","UA","Leather",3456,
        ... Purpose.FIELDPLAYER, 45))
        >>> list_of_founded_goods_by_producer = club_manager.find_goods_by_producer("Lion")
        >>> len(list_of_founded_goods_by_producer)
        1
        """
        list_of_founded_goods: List[Good] = []
        for good in self.list_of_goods:
            if good.producer == producer:
                list_of_founded_goods.append(good)
        return list_of_founded_goods


if __name__ == '__main__':
    testmod(verbose=True)
