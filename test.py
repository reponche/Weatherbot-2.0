import unittest
from get_temp import conv_farh_to_cels

class TestGetTemp(unittest.TestCase):

    fahr = 50

    def test_conv_farh_to_cels(fahr):
        cels = conv_farh_to_cels(fahr)
        self.assertEqual(conv_farh_to_cels(fahr, cels)


if __name__ == '__main__' :
    unittest.main()
