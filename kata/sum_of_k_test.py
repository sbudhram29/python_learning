import unittest
import sum_of_k as kSum


class kSum_test(unittest.TestCase):

    def test_kSum(self):

        self.assertEqual(kSum.sum_of_k([10, 1, 2, 3, 4, 9], 19), True)
        self.assertEqual(kSum.sum_of_k([10, 1, 2, 3, 4, 9], 99), False)
        self.assertEqual(kSum.sum_of_k([10, 1, 2, 3, 4, 9], 14), True)
        self.assertEqual(kSum.sum_of_k([10, 1, 2, 3, 4, 9], 13), True)
        self.assertEqual(kSum.sum_of_k([10, 1, 2, 3, 4, 9], 6), True)


if __name__ == '__main__':
    unittest.main()
