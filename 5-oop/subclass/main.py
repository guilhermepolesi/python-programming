# A stack from scratch

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


# Now, let's go a little further. Let's add a new class to handle stacks.
#
# The new class must be able to evaluate the sum of all elements currently stored on the stack.
#
# We do not want to modify the previously defined stack. It is already good enough in its applications, and we do not
# want it to be changed in any way. We want a new stack with new capabilities. In other words, we want to build a
# subclass of the existing Stack class.
#
# The first step is easy: just define a new subclass pointing to the class that will be used as the superclass.
#
# This is what it looks like:

class AddingStack(Stack):
    pass


# The class doesn't yet define any new components, but that doesn't mean it's empty. Receives all components defined by
# its superclass - the name of the superclass is written before the colon, directly after the name of the new class.
#
# This is what we want from the new stack:
#
#     we want the push method not only to push the value to the stack, but also to add the value to the sum variable;
#     we want the pop function not only to remove the value from the stack, but also to subtract the value from the
#     sum variable.
#
#
# Firstly, let's add a new variable to the class. It will be a private variable, like the stack list. We don't want
# anyone to manipulate the sum value.
#
# As you already know, adding a new property to the class is done by the constructor. You already know how to do this
# but there's something really intriguing inside the builder. Take a look:

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


# The second line of the constructor body creates a property called __sum - it will store the total of all values in
# the stack.
#
# But the line before it looks different. What does it do? Is it really necessary? Yes it is.
#
# Unlike many other languages, Python forces you to explicitly invoke a superclass's constructor. Omitting this point
# will have harmful effects - the object will be deprived of the __stack_list list. Such a stack will not work correctly
#
# This is the only time you can explicitly invoke any of the available constructors - it can be done within the subclass
# constructor.
#
# Note the syntax:
#
#     specifies the name of the superclass (this is the class whose constructor you want to execute)
#     puts a period (.) after it;
#     specifies the name of the constructor;
#     it has to point to the object (the class instance) that has to be initialized by the constructor - that's why you
#     have to specify the argument and use the self variable here; note: invoking any method (including constructors)
#     from outside the class never requires placing the self argument in the argument list - invoking a method from
#     within the class requires explicit use of the self argument, and must be placed first place on the list.
#
# Note: It is generally best practice to invoke the superclass constructor before any other initializations you want to
# perform within the subclass. This is the rule we have been following in the snippet.


# Secondly, let's add two methods. But let us ask you: are you really adding? We already have these methods in the
# superclass. Can we do something like this?
#
# Yes we can. This means that we will change the functionality of the methods, not their names. We can say more
# precisely that the interface (the way objects are handled) of the class remains the same when changing the
# implementation at the same time.

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    # Let's start with the implementation of the push function. This is what we expect from her:
    #
    #     add the value to the __sum variable;
    #     push the value to the stack.
    #
    # Note: the second activity has already been implemented within the superclass - so we can use it.
    # Furthermore, we have to use it since there is no other way to access the __stackList variable.
    #
    # This is what the push method looks like in the subclass:
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    #
    #
    # Note the way we invoked the previous implementation of the push method (the one available in the superclass):
    #
    #     we have to specify the name of the superclass; this is necessary to clearly indicate the class containing the
    #     method, to avoid confusing it with any other function of the same name;
    #     we must specify the target object and pass it as the first argument (it is not implicitly added to the invocation
    #     in this context).
    #
    # We say that the push method has been deprecated - the same name in the superclass now represents a different
    # functionality.

    # This is the new pop function:
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    #
    #
    # So far, we have defined the __sum variable, but we have not provided a method to obtain its value. It appears to
    # be hidden. How can we reveal it and do so in a way that still protects it from modification?
    #
    # We have to define a new method. Let's name it get_sum. Your only task will be to return the __sum value.
    #
    # Here it is:
    def get_sum(self):
        return self.__sum


# So let's look at the program. The complete code for the class. We can verify its operation now, and we do so with the
# help of very few additional lines of code.

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
