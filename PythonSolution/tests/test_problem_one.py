from models import CabinPrice, Rate, BestGroupPrice
from unittest import TestCase

from solutions.problem_one import get_best_group_prices


class TestProblemOne(TestCase):
    def test_get_best_group_prices_basic(self):
        rates = [Rate("M1", "Military"), Rate("S1", "Senior")]
        cabin_prices = [
            CabinPrice("C1", "M1", 100),
            CabinPrice("C1", "S1", 150),
            CabinPrice("C2", "M1", 200),
            CabinPrice("C2", "S1", 250),
        ]
        expected = [
            BestGroupPrice("C1", "M1", 100, "Military"),
            BestGroupPrice("C2", "M1", 200, "Military"),
            BestGroupPrice("C1", "S1", 150, "Senior"),
            BestGroupPrice("C2", "S1", 250, "Senior"),
        ]
        self.assertEqual(get_best_group_prices(rates, cabin_prices), expected)

    def test_get_best_group_prices_best_price(self):
        rates = [Rate("M1", "Military"), Rate("S1", "Senior")]
        cabin_prices = [
            CabinPrice("C1", "M1", 300),
            CabinPrice("C1", "M1", 100),  # Best price for C1 in Military
            CabinPrice("C1", "S1", 150),
            CabinPrice("C2", "M1", 250),
            CabinPrice("C2", "S1", 150),  # Best price for C2 in Senior
            CabinPrice("C2", "S1", 200),
        ]
        expected = [
            BestGroupPrice("C1", "M1", 100, "Military"),
            BestGroupPrice("C2", "M1", 250, "Military"),
            BestGroupPrice("C1", "S1", 150, "Senior"),
            BestGroupPrice("C2", "S1", 150, "Senior"),
        ]
        self.assertEqual(get_best_group_prices(rates, cabin_prices), expected)

    def test_get_best_group_prices_empty_input(self):
        # Testing with empty lists
        assert get_best_group_prices([], []) == []

    def test_nonexistent_rate_codes(self):
        rates = [Rate("M1", "Military")]
        cabin_prices = [CabinPrice("C1", "M2", 300)]  # M2 is not defined in rates
        expected = []  # Expecting empty list since there is no matching rate
        result = get_best_group_prices(rates, cabin_prices)
        self.assertEqual(result, expected)

    def test_duplicate_cabin_prices(self):
        rates = [Rate("M1", "Military")]
        cabin_prices = [
            CabinPrice("C1", "M1", 300),
            CabinPrice("C1", "M1", 200),  # Duplicate with a lower price
        ]
        expected = [BestGroupPrice("C1", "M1", 200, "Military")]
        self.assertEqual(get_best_group_prices(rates, cabin_prices), expected)

    def test_rates_with_no_cabin_prices(self):
        rates = [Rate("M1", "Military"), Rate("S1", "Senior")]
        cabin_prices = []  # No prices available
        expected = []  # Expecting empty list since there are no prices
        self.assertEqual(get_best_group_prices(rates, cabin_prices), expected)

    def test_all_rates_same_group(self):
        rates = [Rate("M1", "Military"), Rate("M2", "Military")]
        cabin_prices = [CabinPrice("C1", "M1", 100), CabinPrice("C2", "M2", 150)]
        expected = [
            BestGroupPrice("C1", "M1", 100, "Military"),
            BestGroupPrice("C2", "M2", 150, "Military"),
        ]
        self.assertEqual(get_best_group_prices(rates, cabin_prices), expected)

    def test_invalid_price_values(self):
        rates = [Rate("M1", "Military")]
        cabin_prices = [
            CabinPrice("C1", "M1", -100),  # Invalid negative price
            CabinPrice("C2", "M1", 0),  # Zero price
        ]
        # Expected behavior might vary; here we assume it filters out invalid prices
        expected = [BestGroupPrice("C2", "M1", 0, "Military")]
        self.assertEqual(get_best_group_prices(rates, cabin_prices), expected)
