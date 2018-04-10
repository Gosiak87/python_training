import unittest
from functions import div


# def div(a, b):
 #   return a / b


class TestDiv(unittest.TestCase):
    def test_divide_by_zero(self):
        self.assertIsNone(div(1, 0))

    def test_divide_by_string(self):
        self.assertIsNone(div(2, "nic"))
        self.assertIsNone(div("cos", "nic"))
        self.assertIsNone(div("cos", 1))

    def test_divide_by_float(self):
        self.assertEqual(div(2, 0.5), 4)
        self.assertEqual(div(0.5, 4), 0.125)
        self.assertEqual(div(0.5, 0.5), 1)


if __name__ == "__main__":   # do uruchomienia testów
    unittest.main()

