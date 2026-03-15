from queue import Queue

EVENT_QUEUE = Queue()

def publish(event):
    EVENT_QUEUE.put(event)

def get_event():
    if EVENT_QUEUE.empty():
        return None
    return EVENT_QUEUE.get()
