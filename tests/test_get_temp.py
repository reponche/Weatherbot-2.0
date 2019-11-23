import unittest
from weatherbot.get_temp import get_weather, conv_kelv_to_cels, add_C

class TestGetTemp(unittest.TestCase):

    def test_get_weather_type(self):
        a = get_weather("Moscow", OWN_TOKEN)
        self.assertIsInstance(a, int)

    def test_conv_kelv_to_cels(self):
        kelv = 70
        cels = conv_kelv_to_cels(kelv)
        self.assertEqual(cels, -203)

    def test_add_C(self):
        cels = "10"
        temp = add_C(cels)
        self.assertEqual(temp, "10°C".encode('utf-8'))

if __name__ == "__main__" :
    unittest.main()
