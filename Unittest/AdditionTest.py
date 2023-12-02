import unittest
from Operators import Addition as a

class Addition_test(unittest.TestCase):
    def testcases(self):
        self.assertAlmostEqual(a.Addition(1, 1), 2)
        self.assertAlmostEqual(a.Addition(-1, 1), 0)
        self.assertAlmostEqual(a.Addition(10, 10), 20)
        self.assertAlmostEqual(a.Addition(1000, -1000), 0)
        self.assertAlmostEqual(a.Addition(10.2, 10.3), 20.5)

