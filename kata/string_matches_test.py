import unittest
import string_matches as match


class string_matches_test(unittest.TestCase):

    def test_longest_match(self):
        self.assertEqual(match.find_longest('ABAXDC', 'BACBAD'), 'ABAD')
        self.assertEqual(match.find_longest('aaaa', 'aa'), 'aa')
        self.assertEqual(match.find_longest('AGGTAB', 'GCTXAYB'), 'GTAB')
        self.assertEqual(match.find_longest('seanbudhram', 'sxecadn'), 'sean')
        self.assertEqual(match.find_longest('seanbudhram', 'seanbudhram'), 'seanbudhram')
        self.assertEqual(match.find_longest('sbudhram', 'sbudhram'), 'sbudhram')


if __name__ == '__main__':
    unittest.main()
