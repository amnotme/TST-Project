from dataclasses import dataclass


@dataclass
class BestGroupPrice:

    cabin_code: str
    rate_code: str
    price: float
    rate_group: str
