from unittest import TestCase
from models import Promotion, PromotionCombo
from solutions.problem_two import all_combinable_promotions, combinable_promotions


class TestProblemTwo(TestCase):

    def setUp(self):
        self.sample_promotions = [
            Promotion(code="A", not_combinable_with=["B"]),
            Promotion(code="B", not_combinable_with=[]),
            Promotion(code="C", not_combinable_with=["A"]),
        ]

        self.sample_promotion_combos = [
            PromotionCombo(["A", "C"]),
            PromotionCombo(["B"]),
        ]

        self.sample_promotion_combos_extended = [
            PromotionCombo(["A", "C"]),
            PromotionCombo(["B"]),
            PromotionCombo(["D"]),  # Added another combo for more comprehensive testing
        ]

    def test_all_combinable_promotions(self):
        result = all_combinable_promotions(self.sample_promotions)
        # Convert result to list of lists for easier comparison
        result_codes = [sorted(combo.promotion_codes) for combo in result]
        # Check if the expected combinations are in the results
        self.assertIn(["A"], result_codes)
        self.assertIn(["B", "C"], result_codes)
        self.assertNotIn(["B"], result_codes)
        self.assertNotIn(["C"], result_codes)
        self.assertNotIn(["A", "C"], result_codes)  # A and C cannot be combined

    def test_combinable_promotions(self):
        result = combinable_promotions("A", self.sample_promotion_combos)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].promotion_codes, ["A", "C"])

        # Test for a code that should not be found
        result = combinable_promotions("D", self.sample_promotion_combos)
        self.assertEqual(len(result), 0)

    def test_empty_promotions(self):
        result = all_combinable_promotions([])
        self.assertEqual(result, [])

    def test_single_promotion(self):
        single_promotion = [Promotion(code="Z", not_combinable_with=[])]
        result = all_combinable_promotions(single_promotion)
        result_codes = [combo.promotion_codes for combo in result]
        self.assertEqual(result_codes, [["Z"]])

    def test_all_not_combinable_promotions(self):
        promotions = [
            Promotion(code="E", not_combinable_with=["F", "G"]),
            Promotion(code="F", not_combinable_with=["E", "G"]),
            Promotion(code="G", not_combinable_with=["E", "F"]),
        ]
        result = all_combinable_promotions(promotions)
        result_codes = [sorted(combo.promotion_codes) for combo in result]
        self.assertIn(["E"], result_codes)
        self.assertIn(["F"], result_codes)
        self.assertIn(["G"], result_codes)
        self.assertNotIn(["E", "F"], result_codes)
        self.assertNotIn(["E", "G"], result_codes)
        self.assertNotIn(["F", "G"], result_codes)

    def test_specific_promotion_code_combinations(self):
        # Test for a code that should be found in multiple combinations
        result = combinable_promotions("B", self.sample_promotion_combos_extended)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].promotion_codes, ["B"])

        # Adding new promotion combinations and testing
        new_combos = self.sample_promotion_combos_extended + [
            PromotionCombo(["B", "D"])
        ]
        result = combinable_promotions("B", new_combos)
        self.assertEqual(len(result), 2)
        self.assertIn(["B", "D"], [combo.promotion_codes for combo in result])
