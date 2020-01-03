import unittest

from weatherbot.puller import should_add, get_new

class TestPuller(unittest.TestCase):

    def test_should_add_true(self):
        self.assertEqual(should_add({"message": "Foo", "id": 3}, 1), True)

    def test_should_add_false(self):
        self.assertEqual(should_add({"message": "Foo", "id": 3}, 4), False)

    def test_get_new(self):
        elems = [{"message": "/start","id": 1},{"message": "London, UK","id": 2},{"message": "/weather","id": 3},{"message": "message","id": 4},{"message": "Moscow","id": 5}]
        test_elems = [{"message": "/weather","id": 3}, {"message": "message","id": 4}, {"message": "Moscow","id": 5}]
        self.assertEqual(get_new(elems, 2), test_elems)
        self.assertEqual(get_new(elems, 5), [])

if __name__ == "__main__" :
    unittest.main()
