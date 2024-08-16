# A queue (queue) is a data model characterized by the term FIFO: First In - Fist Out. Note: a regular queue (queue)
# that you know from stores or post offices works exactly the same way - a customer who arrived first is also served
# first.
#
# Your task is to implement the Queue class with two basic operations:
#
#     put(element), which places an element at the end of the queue;
#     get(), which takes an element from the front of the queue and returns it as a result (the queue cannot be empty
#     to execute it successfully.)
#
# Follow the tips:
#
#     use a list as your storage (just like we did in the stack)
#     put() must append elements to the beginning of the list, while get() must remove elements from the end of
#     the list;
#     define a new exception called QueueError (choose an exception to derive from) and raise it when get() tries
#     to operate on an empty list.

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            val = self.__queue[-1]
            del self.__queue[-1]
            return val
        else:
            raise QueueError("Queue is empty.")


queue = Queue()
queue.put(1)
queue.put("dog")
queue.put(False)
try:
    for i in range(4):
        print(queue.get())

    raise QueueError
except QueueError as e:
    print("Queue error.", e)
