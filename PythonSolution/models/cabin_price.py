from dataclasses import dataclass


@dataclass
class CabinPrice:

    cabin_code: str
    rate_code: str
    price: float
