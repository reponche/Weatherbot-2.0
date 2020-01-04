import unittest
from collections import deque

from weatherbot.puller import should_add, get_new, add_queue

class TestPuller(unittest.TestCase):

    def test_should_add_true(self):
        self.assertEqual(should_add({"message": "Foo", "update_id": 3}, 1), True)

    def test_should_add_false(self):
        self.assertEqual(should_add({"message": "Foo", "update_id": 3}, 4), False)

    def test_get_new(self):
        updates = [{"message": "/start","update_id": 1},{"message": "London, UK","update_id": 2},{"message": "/weather","update_id": 3},{"message": "message","update_id": 4},{"message": "Moscow","update_id": 5}]
        expectation = [{"message": "/weather","update_id": 3}, {"message": "message","update_id": 4}, {"message": "Moscow","update_id": 5}]
        self.assertEqual(get_new(updates, 2), expectation)
        self.assertEqual(get_new(updates, 123456789), [])

    def test_get_new_unordered(self):
        updates = [{"message": "Moscow","update_id": 5}, {"message": "/start","update_id": 1},{"message": "/weather","update_id": 3}, {"message": "London, UK","update_id": 2},{"message": "message","update_id": 4}]
        expectation = [{"message": "Moscow","update_id": 5}, {"message": "message","update_id": 4}]
        self.assertEqual(get_new(updates, 3), expectation)

    def test_add_queue(self):
        updates = [{"message": "Moscow","update_id": 5}, {"message": "/start","update_id": 1},{"message": "/weather","update_id": 3}, {"message": "London, UK","update_id": 2},{"message": "message","update_id": 4}]
        queue = deque()
        elems_list = get_new(updates, 4)
        self.assertEqual(add_queue(queue, elems_list), deque([{"message": "Moscow","update_id": 5}]))

if __name__ == "__main__" :
    unittest.main()
