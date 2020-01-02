def check_add(dict, id):
    return id < dict["id"]

def get_new(dict, id):
    for item in dict:
        result = check_add(item, id)
        if result:
            print(item)
            pass

def should_add(dict, id):
    queue = []
    return queue.append(get_new(dict, id))
