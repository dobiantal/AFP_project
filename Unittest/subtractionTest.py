import unittest
from subtraction import subtract


class TestSubtraction(unittest.TestCase):

    def test_accuracy(self):
        # Teszteli, hogy az eredmény 8 tizedesjegy pontossággal van-e kerekítve
        eredmeny, hiba = subtract("10.12345678", "3.98765432")
        self.assertEqual(eredmeny, 6.13580246)
        self.assertIsNone(hiba)

    def test_error(self):
        # Teszteli, hogy a hiba esetén a függvény hibaüzenetet ad vissza
        eredmeny, hiba = subtract("abc", "3.98765432")
        self.assertIsNone(eredmeny)
        self.assertEqual(hiba, "Hiba történt a kivonás során: Invalid literal for Decimal: 'abc'")

    def test_with_zero_extract(self):
        # Teszteli, hogy nullával való kivonás helyes eredményt ad
        eredmeny, hiba = subtract("10.12345678", "0")
        self.assertEqual(eredmeny, 10.12345678)
        self.assertIsNone(hiba)

    def test_negativ_extract(self):
        # Teszteli, hogy negatív számmal való kivonás helyes eredményt ad
        eredmeny, hiba = subtract("-5.5", "3.5")
        self.assertEqual(eredmeny, -9)
        self.assertIsNone(hiba)

    def test_floating_point_result(self):
        # Teszteli, hogy lebegőpontos eredményt ad-e vissza, ha a kivonás eredménye tört
        eredmeny, hiba = subtract("5", "2")
        self.assertEqual(eredmeny, 3.0)
        self.assertIsNone(hiba)

    def test_decimals_rounded(self):
        # Teszteli, hogy helyesen kerekíti-e a kivonás eredményének tizedesjegyeket
        eredmeny, hiba = subtract("7.12345678", "3.98765432")
        self.assertEqual(eredmeny, 3.13580246)
        self.assertIsNone(hiba)

    def test_same_number(self):
        # Teszteli, hogy nullával való kivonás helyes eredményt ad
        eredmeny, hiba = subtract("10", "10")
        self.assertEqual(eredmeny, 0)
        self.assertIsNone(hiba)


if __name__ == '__main__':
    unittest.main()
