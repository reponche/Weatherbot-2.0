import unittest
from get_temp import conv_farh_to_cels
from get_temp import add_C

class TestGetTemp(unittest.TestCase):

    def test_conv_farh_to_cels(self):
        self.assertEqual(conv_farh_to_cels(50), 10.0)

    def test_add_C(self):
        self.assertEqual(add_C(50), "50℃")

if __name__ == '__main__':
    unittest.main()
