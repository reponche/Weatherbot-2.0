from collections import deque

def should_add(updates, update_id):
    return update_id < updates["update_id"]

def get_new(updates, update_id):
    buffer = []
    for item in updates:
        if should_add(item, update_id):
            buffer.append(item)
    return buffer

def add_queue(queue, elems_list):
    for item in elems_list:
        queue.append(item)
    return queue
