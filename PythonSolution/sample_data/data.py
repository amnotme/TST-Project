from models import Rate, CabinPrice, BestGroupPrice
from typing import List
from constants import RateGroups as RG, CabinCodes as CC, RateCodes as RC


def get_input_rates() -> List[Rate]:
    return [
        Rate(RC.M1, RG.MI),
        Rate(RC.M2, RG.MI),
        Rate(RC.S1, RG.SE),
        Rate(RC.S2, RG.SE),
    ]


def get_input_cabin_prices() -> List[CabinPrice]:
    return [
        CabinPrice(CC.CA, RC.M1, 200.00),
        CabinPrice(CC.CA, RC.M2, 250.00),
        CabinPrice(CC.CA, RC.S1, 225.00),
        CabinPrice(CC.CA, RC.S2, 260.00),
        CabinPrice(CC.CB, RC.M1, 230.00),
        CabinPrice(CC.CB, RC.M2, 260.00),
        CabinPrice(CC.CB, RC.S1, 245.00),
        CabinPrice(CC.CB, RC.S2, 270.00),
    ]
