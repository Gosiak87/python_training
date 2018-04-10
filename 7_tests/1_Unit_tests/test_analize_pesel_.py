import unittest
from functions import analyze_pesel
from datetime import datetime

# def div(a, b):
 #   return a / b


class TestAnalizePesel(unittest.TestCase):
    def test_pesel_with_string(self):
        bad_pesel ='12a456vb901'
        self.assertIsNone(analyze_pesel(bad_pesel))

    def test_pesel_after_1999(self):
        pesel = "00211204615"
        result = analyze_pesel(pesel)
        birth_date = datetime(2000, 1, 12)
        self.assertEqual(result['birth_date'], birth_date)

    def test_pesel_before_2000(self):
        pesel = "99011207913"
        result = analyze_pesel(pesel)
        birth_date = datetime(1999, 1, 12)
        self.assertEqual(result['birth_date'], birth_date)

    def test_pesel_gender(self):
        pesel_women = '99011216908'
        pesel_man = '99011246716'
        result_women = analyze_pesel(pesel_women)
        result_man = analyze_pesel(pesel_man)
        self.assertEqual(result_women['gender'], 'female')
        self.assertEqual(result_man['gender'], 'male')

    def test_short_pesel(self):
        short_pesel = ''
        self.assertIsNone(analyze_pesel(short_pesel))
        long_pesel = '11111111111111111'
        self.assertIsNone(analyze_pesel(long_pesel))

    def test_pesel_is_valid(self):
        valid_pesel = '99011216908'
        invalid_pesel = '11111111111'
        result_valid = analyze_pesel(valid_pesel)
        result_invalid = analyze_pesel(invalid_pesel)
        self.assertTrue(result_valid['valid'])
        self.assertFalse(result_invalid['valid'])

    def test_pesel_greater_31(self):
        valid_pesel = '99014416908' # day 44
        self.assertIsNone(analyze_pesel(valid_pesel))


if __name__ =="__main__":  # do uruchomienia testów
    unittest.main()
