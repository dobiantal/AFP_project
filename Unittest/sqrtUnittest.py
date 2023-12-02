import unittest

from Operators.sqrt import negyzetgyok


class TestNegyzetgyok(unittest.TestCase):

    def test_negyzetgyok(self):
        # Tesztesetek:
        self.assertAlmostEqual(negyzetgyok(16), 4.0)  # 16 négyzetgyöke 4
        self.assertAlmostEqual(negyzetgyok(25), 5.0)  # 25 négyzetgyöke 5
        self.assertAlmostEqual(negyzetgyok(9), 3.0)   # 9 négyzetgyöke 3
        self.assertAlmostEqual(negyzetgyok(-12), 0)  # -12 négyzetgyöke 0
        self.assertAlmostEqual(negyzetgyok(14), 3.7416573867739413)  # nem egészre visszatérő érték ellenörzése
        self.assertAlmostEqual(negyzetgyok(4.5), 2.1213203435596424)  # nem egészre visszatérő érték ellenörzése




