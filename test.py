import unittest
from get_temp import conv_farh_to_cels
from get_temp import add_C

class TestGetTemp(unittest.TestCase):

    def test_conv_farh_to_cels(self):
        fahr = 50
        cels = conv_farh_to_cels(fahr)
        self.assertEqual(cels, 10.0)

    def test_add_C(self):
        cels = "10.0"
        temp = add_C(cels)
        self.assertEqual(temp, "10.0C")


if __name__ == "__main__" :
    unittest.main()
