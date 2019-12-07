import unittest
from weatherbot.telegram import get_updates, get_message, get_update_id, send_message

class TestGetTemp(unittest.TestCase):

data = get_updates()

    def test_get_message(self):
        message = get_message(data)
        self.assertIsInstance(message, str)

if __name__ == "__main__" :
    unittest.main()
