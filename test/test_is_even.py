from unittest import TestCase
from src.is_even import Plays


class Test(TestCase):
    # pass
    def test_even_numbers(self):
        my_even = Plays
        self.assertEqual([2, 4, 6, 8, 10], my_even.even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_odd_numbers(self):
        my_odd = Plays
        self.assertEqual([1, 3, 5, 7, 9], my_odd.odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
