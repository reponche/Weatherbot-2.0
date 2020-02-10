import unittest
import tempfile

from weatherbot.state import *

class TestPuller(unittest.TestCase):

    def test_get_new(self):
        updates = [{"message": "/start","update_id": 1},{"message": "London, UK","update_id": 2},{"message": "/weather","update_id": 3},{"message": "message","update_id": 4},{"message": "Moscow","update_id": 5}]
        expectation = [{"message": "/weather","update_id": 3}, {"message": "message","update_id": 4}, {"message": "Moscow","update_id": 5}]
        self.assertEqual(get_new(updates, 2), expectation)
        self.assertEqual(get_new(updates, 123456789), [])

    def test_get_new_unordered(self):
        updates = [{"message": "Moscow","update_id": 5}, {"message": "/start","update_id": 1},{"message": "/weather","update_id": 3}, {"message": "London, UK","update_id": 2},{"message": "message","update_id": 4}]
        expectation = [{"message": "Moscow","update_id": 5}, {"message": "message","update_id": 4}]
        self.assertEqual(get_new(updates, 3), expectation)

    def test_get_elems(self):
        updates = [{"message": "/start","update_id": 1},{"message": "London, UK","update_id": 2},{"message": "/weather","update_id": 3}]
        state_file = tempfile.mktemp("weather-bot")
        puller = State(state_file)
        puller.filter(updates)
        queue = puller.get_elems()
        expectation = [{"message": "/start","update_id": 1}, {"message": "London, UK","update_id": 2}, {"message": "/weather","update_id": 3}]
        self.assertEqual(queue, expectation)

    def test_get_state_nonexistent(self):
        state_file = tempfile.mktemp("weather-bot")
        state = get_state(state_file)
        expectation = 0
        self.assertEqual(state, expectation)

    def test_get_state_existent(self):
        (state_fd, state_file) = tempfile.mkstemp("weather-bot", text=True)
        state_handle = open(state_fd, 'w')
        state_handle.write("42")
        state_handle.close()

        state = get_state(state_file)
        expectation = 42
        self.assertEqual(state, expectation)


if __name__ == "__main__":
    unittest.main()
