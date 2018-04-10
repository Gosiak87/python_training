import unittest
from calculator import calculate_vat

class VatCalculatorTest(unittest.TestCase):
    def test_normal_vat(self):
        vat = 0.23
        price = 100
        self.assertEqual(calculate_vat(price, vat), 23, "Powinno być 23 zł")

    def test_string_as_price(self):
        vat = 0.23
        price = 'Nie pamiętam'
        self.assertIsNone(calculate_vat(price, vat))

    def test_string_as_vat(self):
        vat = 'Nie pamiętam'
        price = 100
        self.assertIsNone(calculate_vat(price, vat))

    def test_string_as_price_vat(self):
        vat = 'Bardzo duzy'
        price = 'Nie pamiętam'
        self.assertIsNone(calculate_vat(price, vat))

    def test_negative_vat_take_23_percent(self):
        vat = - 0.2
        price = 100
        self.assertEqual(calculate_vat(price, vat), 23)

    def test_vat_is_unset_take_23_percent(self):
        price = 100
        self.assertEqual(calculate_vat(price), 23)
