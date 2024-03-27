from sample_data import get_input_promotions
from models import PromotionCombo, Promotion
from typing import List, Tuple
from itertools import combinations


def all_combinable_promotions(
    all_promotions: List[Promotion],
) -> List[PromotionCombo]:
    # 1. Iterates through all possible combinations of all the promotions
    # 2. Identifies if the combination is valid
    # 3. Filters possible maximal combinations (that is, all combinations without repeating of longest possible length)
    # 4. Converts maximal combinations back to a list creates instances of PromotionCombo
    maximal_combos = []
    potential_combos = []
    for idx in range(1, len(all_promotions) + 1):
        for combination in combinations(all_promotions, idx):
            combination_list = [combo.code for combo in combination]
            if _is_combination_valid(combos=combination):
                potential_combos.append(set(combination_list))

    _get_maximal_combinations(
        potential_combinations=potential_combos, maximal_combos=maximal_combos
    )

    return [PromotionCombo(sorted(list(combo))) for combo in maximal_combos]


def _get_maximal_combinations(
    potential_combinations: List, maximal_combos: List
) -> None:
    # Filter out non-maximal combinations from the potential combinations.
    for combo in potential_combinations:
        maximal_combo = True
        for other_combo in potential_combinations:
            if other_combo != combo and combo.issubset(other_combo):
                maximal_combo = False
                break
        if maximal_combo:
            maximal_combos.append(combo)


def _is_combination_valid(combos: Tuple[Promotion]) -> bool:
    # Check if a given combination of promotions is valid (i.e., all promotions can be combined).
    # 1. It iterates through a tuple of possible combinations and checks that:
    # 2.a PromoCode from isn't in any other not_combinable_with list from evey other Promotion
    for i, promo in enumerate(combos):
        # Avoid comparing a promotion with itself and ensure each pair is checked only once.
        for promo_two in combos[i + 1:]:
            if (
                promo_two.code in promo.not_combinable_with
                or promo.code in promo_two.not_combinable_with
            ):
                return False  # If any pair is not combinable, the whole combination is not valid.
    return True


def combinable_promotions(
    promotion_code: str,
    all_promotions: List[PromotionCombo],
) -> List[PromotionCombo]:
    # 1. Given a list of PromotionCombos, it returns a list of filtered PromotionCombos that match the promotion_code
    return [
        promotion
        for promotion in all_promotions
        if promotion_code in promotion.promotion_codes
    ]


def problem_two_run() -> None:
    # Wrapper function to run problem two
    all_combinable_promotions_solution = all_combinable_promotions(
        all_promotions=get_input_promotions()
    )
    for solution in all_combinable_promotions_solution:
        print(f"{all_combinable_promotions.__name__}  =>", solution)

    for solution in combinable_promotions(
        promotion_code="P1", all_promotions=all_combinable_promotions_solution
    ):
        print(f"{combinable_promotions.__name__} 'P1' =>", solution)

    for solution in combinable_promotions(
        promotion_code="P3", all_promotions=all_combinable_promotions_solution
    ):
        print(f"{combinable_promotions.__name__} 'P3' =>", solution)


if __name__ == "__main__":
    problem_two_run()
