import unittest
from hash_password import hash_password

class Hash_PasswordTest(unittest.TestCase):
    def test_shorter_number_of_password(self):
        shorter_password ='1238'
        self.assertIsNone(hash_password(shorter_password))

    def test_no_big_letter_password(self):
        no_big_letter_password = 'alamarozowegokota'
        self.assertIsNone(hash_password(no_big_letter_password))

    def test_no_small_letter_password(self):
        small_letter_password = 'ALAMAROZOWE'
        self.assertIsNone(hash_password(small_letter_password))

    def test_no_number(self):
        no_number_password = 'LALAmkjsa'
        self.assertIsNone(hash_password(no_number_password))

    def test_no_special(self):
        no_special_password = 'ALAmaki1'
        self.assertIsNone(hash_password(no_special_password))

    def test_good_passw(self):
        password = 'Az7$rtu'
        self.assertTrue(hash_password(password))

