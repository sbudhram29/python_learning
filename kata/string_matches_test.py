import unittest
import string_matches as match


class string_matches_test(unittest.TestCase):

    def test_longest_match(self):
        self.assertEquals(match.find_longest('ABAXDC', 'BACBAD'), 'ABAD')
        self.assertEquals(match.find_longest('aaaa', 'aa'), 'aa')
        self.assertEquals(match.find_longest('AGGTAB', 'GCTXAYB'), 'GTAB')


if __name__ == '__main__':
    unittest.main()
