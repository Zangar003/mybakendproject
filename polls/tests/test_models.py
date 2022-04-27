from django.test import TestCase
from ..models import *;

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test_compare_numbers(self):
        print('test_compare_numbers')
        post = Author()
        self.assertEqual(post.get_number(), 10)

    def test_get_boolean(self):

        print("test: test_get_boolean")
        self.assertTrue(True)

    def test_get_length(self):
        print("test: test_get_length")
        fin = Author()
        self.assertEqual(fin.get_length(), 8)
