import unittest
from weatherbot.get_temp import conv_farh_to_cels, add_C, get_weather
from weatherbot.tokens import OWN_TOKEN

class TestGetTemp(unittest.TestCase):

    def test_get_weather_type(self):
        a = get_weather("Moscow", OWN_TOKEN)
        self.assertIsInstance(a, int)

    def test_conv_farh_to_cels(self):
        fahr = 50
        cels = conv_farh_to_cels(fahr)
        self.assertEqual(cels, 10.0)

    def test_add_C(self):
        cels = "10"
        temp = add_C(cels)
        self.assertEqual(temp, "10°C".encode('utf-8'))

if __name__ == "__main__" :
    unittest.main()
