from collections import deque
import os.path


def should_add(updates, update_id):
    return update_id < updates["update_id"]


def get_new(updates, update_id):
    buffer = []
    for item in updates:
        if should_add(item, update_id):
            buffer.append(item)
    return buffer


def get_state(state_file):
    if not os.path.exists(state_file):
        with open(state_file, 'x') as f:
            f.write("0")
            return 0
    else:
        with open(state_file, 'r') as f:
            state_str = int(f.read())
            return state_str


def write_state(state_file, state):
    if state_file is not None:
        with open(state_file, 'w') as f:
            f.write(str(state))


class Puller:
    """In class Puller we create deque() object.
    We need state of deque() and last update_id of deque()."""

    def __init__(self, state_file=None):
        self.queue = deque()
        self.state_file = state_file
        if state_file is None:
            self.update_id = 0
        else:
            self.update_id = get_state(state_file)

    def pull(self, updates):
        data = get_new(updates, self.update_id)
        for elem in data:
            self.queue.append(elem)
            update_id = elem["update_id"]
            write_state(self.state_file, update_id)
            self.update_id = update_id

    def get_elems(self):
        buffer = []
        while len(self.queue) > 0:
            first = self.queue.popleft()
            buffer.append(first)
        return buffer
