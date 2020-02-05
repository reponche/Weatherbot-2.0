from collections import deque


def should_add(updates, update_id):
    return update_id < updates["update_id"]


def get_new(updates, update_id):
    buffer = []
    for item in updates:
        if should_add(item, update_id):
            buffer.append(item)
    return buffer


class Puller:
    """In class Puller we create deque() object.
    We need state of deque() and last update_id of deque()."""

    def __init__(self):
        self.queue = deque()
        self.update_id = 0

    def pull(self, updates):
        data = get_new(updates, self.update_id)
        for elem in data:
            self.queue.append(elem)
            self.update_id = elem["update_id"]

    def get_elems(self):
        buffer = []
        while len(self.queue) > 0:
            first = self.queue.popleft()
            buffer.append(first)
        return buffer
