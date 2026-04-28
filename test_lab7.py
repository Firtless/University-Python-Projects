import unittest
import os
from lab7 import min_cable


class TestTelecomCable(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_wells.csv'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_standard_connection(self):
        with open(self.test_file, 'w') as f:
            f.write("K1, K2, 100\nK2, K3, 150\nK1, K3, 300")
        self.assertEqual(min_cable(self.test_file), 250)

    def test_disconnected_wells(self):
        with open(self.test_file, 'w') as f:
            f.write("K1, K2, 100\nK3, K4, 200")
        self.assertEqual(min_cable(self.test_file), -1)

    def test_empty_file(self):
        with open(self.test_file, 'w') as f:
            f.write("")
        self.assertEqual(min_cable(self.test_file), 0)


if __name__ == '__main__':
    unittest.main()
