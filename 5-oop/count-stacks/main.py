# Your task is to extend the behavior of the Stack class so that the class is able to count all elements that are pushed
# and popped (we assume that the pop count is sufficient). Use the Stack class

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


# Follow the tips:
#
#     introduce a property designed to count pop operations and name it in a way that ensures its hiding;
#     initialize it to zero inside the constructor;
#     provide a method that returns the value currently assigned to the counter (name it get_counter()).


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count_pop = 0

    def get_counter(self):
        return self.__count_pop

    def pop(self):
        val = Stack.pop(self)
        self.__count_pop += 1
        return val


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
