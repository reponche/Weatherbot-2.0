import unittest
from weatherbot.puller import should_add, get_new

class TestGetTemp(unittest.TestCase):

    def test_should_add_true(self):
        a = should_add({"message": "Foo", "id": 3}, 1)
        self.assertEqual(a, True)

    def test_should_add_false(self):
        a = should_add({"message": "Foo", "id": 3}, 4)
        self.assertEqual(a, False)

    def test_get_new(self):
        dict = [{"message": "/start","id": 1},{"message": "London, UK","id": 2},{"message": "/weather","id": 3},{"message": "message","id": 4},{"message": "Moscow","id": 5}]
        self.assertEqual(get_new(dict, 2), '{"message": "/weather","id": 3} {"message": "message","id": 4} {"message": "Moscow","id": 5}')
        self.assertEqual(get_new(dict, 5), None)


if __name__ == "__main__" :
    unittest.main()
