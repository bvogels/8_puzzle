import unittest

from Grid import Grid


class MyTestCase(unittest.TestCase):
    def test_check_grid_validity1(self):
        numbers = [3, 4, 2, 8, 0, 5, 6, 7, 1]
        self.assertTrue(Grid().check_validity(numbers))

    def test_check_grid_validity2(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(Grid().check_validity(numbers))

    def test_check_grid_validity3(self):
        numbers = [0, 3, 6, 1, 4, 5, 8, 2, 7]
        self.assertTrue(Grid().check_validity(numbers))

    def test_check_grid_validity4(self):
        numbers = [8, 4, 6, 1, 2, 3, 0, 7, 5]
        self.assertFalse(Grid().check_validity(numbers))



if __name__ == '__main__':
    unittest.main()
