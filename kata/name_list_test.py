import unittest
import name_list


class name_list_test(unittest.TestCase):
    def test_namelist(self):
        self.assertEqual(
            name_list.namelist([{'name': 'Bart'}, {'name': 'Lisa'},
                                {'name': 'Maggie'}]), 'Bart, Lisa & Maggie')

        self.assertEqual(name_list.namelist(
            [{'name': 'Bart'}, {'name': 'Lisa'}]),
            'Bart & Lisa')

        self.assertEqual(name_list.namelist(
            [{'name': 'Bart'}]),
            'Bart')


if __name__ == '__main__':
    unittest.main()
