# Your task is to slightly extend the capabilities of the Queue class. We want it to have a parameterless method that
# returns True if the queue is empty and False otherwise.


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        val = self.__queue[-1]
        del self.__queue[-1]
        return val

    def get_queue(self):
        return self.__queue


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def is_empty(self):
        if len(self.get_queue()) == 0:
            return True
        else:
            return False


queue = SuperQueue()
queue.put(1)
queue.put("dog")
queue.put(False)
try:
    for i in range(4):
        if not queue.is_empty():
            print(queue.get())
        else:
            raise QueueError
except QueueError as e:
    print("Queue empty", e)
