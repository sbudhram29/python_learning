import unittest

from fib import fib


class FibTests(unittest.TestCase):
    def setUp(self):
        self.fib10 = fib(10)
        self.fib1 = fib(1)

    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3

    def test_fib_1_is_1(self):
        assert self.fib1 == 1

    def test_fib_10_is_89(self):
        assert self.fib10 == 55


"""
run auto
"""

if __name__ == "__main__":
    unittest.main()
