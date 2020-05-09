import doctest
from typing import List

from ua.lviv.iot.python.model.good import Good
from ua.lviv.iot.python.model.hockey_puck import HockeyPuck
from ua.lviv.iot.python.model.ice_skates import IceSkates
from ua.lviv.iot.python.model.level import Level
from ua.lviv.iot.python.model.protective_clothes import ProtectiveClothes
from ua.lviv.iot.python.model.purpose import Purpose
from ua.lviv.iot.python.model.sorting import SortingType


class ClubManagerUtils:

    @staticmethod
    def sort_goods_by_price_in_ukrainian_hryvnas(goods: List[Good], sorting: SortingType) -> List[Good]:
        """
        Test of correct sorting list by price ascending
        >>> sorted_list_by_price_in_ukrainian_hryvnas_increase = \
        ClubManagerUtils.sort_goods_by_price_in_ukrainian_hryvnas(list_of_goods_to_test, SortingType.INCREASE)
        >>> [good.price_in_ukrainian_hryvnas for good in sorted_list_by_price_in_ukrainian_hryvnas_increase]
        [150, 200, 350, 400]

        Test of correct sorting list by price descending
        >>> sorted_list_by_price_in_ukrainian_hryvnas_decrease = \
        ClubManagerUtils.sort_goods_by_price_in_ukrainian_hryvnas(list_of_goods_to_test, SortingType.DECREASE)
        >>> [good.price_in_ukrainian_hryvnas for good in sorted_list_by_price_in_ukrainian_hryvnas_decrease]
        [400, 350, 200, 150]
        """
        sorted_list_of_goods_by_price_in_ukrainian_hryvnas: List[Good] = []
        if sorting == SortingType.INCREASE:
            sorted_list_of_goods_by_price_in_ukrainian_hryvnas = sorted(goods, key=lambda
                good: good.price_in_ukrainian_hryvnas)
        elif sorting == SortingType.DECREASE:
            sorted_list_of_goods_by_price_in_ukrainian_hryvnas = sorted(goods, key=lambda
                good: good.price_in_ukrainian_hryvnas, reverse=True)
        return sorted_list_of_goods_by_price_in_ukrainian_hryvnas

    @staticmethod
    def sort_goods_by_amount(hockey_puck: List[HockeyPuck], sorting: SortingType) -> List[HockeyPuck]:
        """
        Test of correct sorting list by price ascending
        >>> sorted_list_by_amount_increase = ClubManagerUtils.sort_goods_by_amount(list_of_goods_to_test , SortingType.INCREASE)
        >>> [good.amount for good in sorted_list_by_amount_increase]
        [1260, 2300, 3450, 7500]

        Test of correct sorting list by price descending
        >>> sorted_list_by_amount_decrease = ClubManagerUtils.sort_goods_by_amount(list_of_goods_to_test, SortingType.DECREASE)
        >>> [good.amount for good in sorted_list_by_amount_decrease]
        [7500, 3450, 2300, 1260]
        """
        sorted_list_of_goods_by_amount: List[HockeyPuck] = []
        if sorting == SortingType.INCREASE:
            sorted_list_of_goods_by_amount = sorted(hockey_puck, key=lambda good: good.amount)
        elif sorting == SortingType.DECREASE:
            sorted_list_of_goods_by_amount = sorted(hockey_puck, key=lambda good: good.amount, reverse=True)
        return sorted_list_of_goods_by_amount


if __name__ == '__main__':
    first_good: Good = HockeyPuck("HockeyPuck", 200, "North", "UA", "Ruber", 1260, Purpose.GOALKEEPER, 2)
    second_good: Good = HockeyPuck("HockeyPuck", 350, "North", "UA", "Ruber", 3450, Purpose.GOALKEEPER, 4)
    third_good: Good = HockeyPuck("HockeyPuck", 150, "North", "UA", "Ruber", 2300, Purpose.GOALKEEPER, 1)
    forth_good: Good = HockeyPuck("HockeyPuck", 400, "North", "UA", "Ruber", 7500, Purpose.GOALKEEPER, 3)
    list_of_goods_to_test: List[Good] = [first_good, second_good, third_good, forth_good]
    doctest.testmod(name='sort_goods_by_price', verbose=True)
    doctest.testmod(name='sort_goods_by_size', verbose=True)
