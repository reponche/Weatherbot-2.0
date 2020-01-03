def should_add(updates, id):
    return id < updates["id"]

def get_new(updates, id):
    buffer = []
    for item in updates:
        if should_add(item, id):
            buffer.append(item)
    return buffer
