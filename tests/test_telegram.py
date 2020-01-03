import unittest
from weatherbot.telegram import get_updates, get_message

class TestGetMessage(unittest.TestCase):

    def test_get_message(self):
        data = get_updates()
        message = get_message(data)
        self.assertIsInstance(message, str)

if __name__ == "__main__" :
    unittest.main()
