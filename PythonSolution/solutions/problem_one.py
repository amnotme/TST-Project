from typing import List, Dict, Optional
from models import Rate, CabinPrice, BestGroupPrice
from sample_data import get_input_rates, get_input_cabin_prices
from collections import defaultdict


def get_best_group_prices(
    rates: List[Rate],
    prices: List[CabinPrice]
) -> Optional[List[BestGroupPrice]]:
    # 1. Builds a dictionary grouping prices by rate code.
    # 2. Determines the best prices for each rate group and cabin.
    # 3. Converts the best prices into BestGroupPrice instances.
    rate_group_dict: Dict = {rate.rate_code: rate.rate_group for rate in rates}
    group_prices_dict: Dict = defaultdict(list)
    best_prices: Dict = defaultdict(lambda: float("inf"))
    best_group_prices: Dict = {}

    _build_group_prices_dict(
        group_prices_dict=group_prices_dict,
        prices=prices,
        rate_group_dict=rate_group_dict
    )
    _build_best_group_prices_dict(
        best_group_prices=best_group_prices,
        best_prices=best_prices,
        group_prices_dict=group_prices_dict,
        rate_group_dict=rate_group_dict
    )

    return [

        BestGroupPrice(
            cabin_code=group_key_tuple[0],
            rate_code=group_key_tuple[1],
            price=price,
            rate_group=rate_group_dict.get(group_key_tuple[1]),
        )
        for group_key_tuple, price in best_group_prices.items()
    ]


def _build_best_group_prices_dict(
    best_group_prices: Dict,
    best_prices: Dict,
    group_prices_dict: Dict,
    rate_group_dict: Dict,
) -> None:
    # 1. Iterates through each group and their associated cabin prices.
    # 2. Finds the best price for each cabin in the group.
    # 3. Updates the best price if the current one is lower.
    # 4. Returns the best_group_dict with final best group prices.

    for group_rate_code, group_price_cabin_price in group_prices_dict.items():

        for cabin_price in group_price_cabin_price:
            best_prices[(cabin_price.cabin_code, group_rate_code)] = min(
                best_prices[(cabin_price.cabin_code, group_rate_code)],
                cabin_price.price,
            )

            if (
                cabin_price.price >= 0
                and cabin_price.price <= best_prices[(cabin_price.cabin_code, group_rate_code)]
                and cabin_price.rate_code in rate_group_dict.keys()
            ):
                best_group_prices[(cabin_price.cabin_code, cabin_price.rate_code)] = (
                    cabin_price.price
                )


def _build_group_prices_dict(
    group_prices_dict: Dict,
    prices: List[CabinPrice],
    rate_group_dict: Dict
) -> None:
    # Groups all prices by their rate code.
    for price in prices:
        price_rate_code = rate_group_dict.get(price.rate_code)
        group_prices_dict[price_rate_code].append(price)


def problem_one_run() -> None:
    # Wrapper function to run the problem with sample data.
    for solution in get_best_group_prices(
        rates=get_input_rates(), prices=get_input_cabin_prices()
    ):
        print(solution)

if __name__ == '__main__':
    problem_one_run()