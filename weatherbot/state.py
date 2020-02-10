from collections import deque
import os.path


def get_new(updates, update_id):
    buffer = []
    for item in updates:
        if update_id < item['update_id']:
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


class State:

    def __init__(self, state_file):
        self.queue = deque()
        self.state_file = state_file
        self.update_id = get_state(state_file)

    def filter(self, updates):
        data = get_new(updates, self.update_id)
        for elem in data:
            self.queue.append(elem)
            update_id = elem["update_id"]
            with open(self.state_file, 'w') as f:
                f.write(str(update_id))
            self.update_id = update_id

    def get_elems(self):
        buffer = []
        while len(self.queue) > 0:
            first = self.queue.popleft()
            buffer.append(first)
        return buffer
