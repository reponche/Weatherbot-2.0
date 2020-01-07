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
    def __init__(self):
        self.queue = deque()
        self.update_id = 0

    def pull(self, updates):
        date = get_new(updates, self.update_id)
        for elems in date:
            self.queue.append()
            self.update_id = elem["update_id"]

    def get_elems(self):
        buffer = []
        while len(self.queue) > 0:
            buffer.append(self.queue.pop())
        return buffer

    def get_state(self):
        return self.queue

a = Puller()
print(a.get_elems())
print(a.get_state())
