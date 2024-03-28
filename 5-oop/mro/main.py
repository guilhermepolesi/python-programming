# What is the Method Resolution Order (MRO) and why don't all inheritances make sense?
#
# MRO, in general, is a way (you can call it a strategy) in which a given programming language analyzes the upper part
# of a class hierarchy in order to find the method it currently needs. It's worth pointing out that different languages
# use slightly (or even completely) different MROs. The Python is a unique creature in this regard, however, and its
# customs are a bit specific.
#
# We'll show you how Python's MRO works in two peculiar cases, which are clear examples of problems that can occur when
# you try to use multiple inheritance too recklessly. Let's start with a snippet that may initially seem simple.
# See what we have prepared for you.

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# We are confident that if you analyze the snippet yourself, you will not see any anomalies in it. Yes, you're
# absolutely right - it seems clear and simple, and doesn't raise any concerns. If you run the code, it will produce
# the following predictable output:
# bottom
# middle
# top
#
# No surprises so far. Let's make a small change to this code. Look:

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Can you see the difference? It's hidden in this line:
#
# class Bottom(Middle, Top):
#
# In this exotic way, we transform a very simple code with a clear path of single inheritance into a mysterious enigma
# of multiple inheritances. "Its valid?" one might ask. Yes it is. "How is that possible?" you should ask now, and we
# hope you really feel the need to ask this question.
#
# As you can see, the order in which the two superclasses were listed in parentheses conforms to the code structure:
# the Middle class precedes the Top class, just like in the actual inheritance path.
#
# Despite its strangeness, the sample is correct and works as expected, but it must be stated that this notation does
# not bring any new functionality or additional meaning.
#
# Let's modify the code once again - now let's swap the two superclass names in the Bottom class definition. This is
# what the snippet looks like now:

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# To anticipate your question, we will say that this amendment ruined the code, and that it will no longer work. What
# a shame. The order we try to force (Top, Middle) is incompatible with the inheritance path that is derived from the
# code structure. Python won't like it. This is what we will see:
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle

# We think the message speaks for itself. Python's MRO cannot be bent or violated, not only because that's how Python
# works, but also because it's a rule that you have to obey.

# The diamond problem
#
# The second example of the spectrum of issues that can eventually arise from multiple inheritance is illustrated by a
# classic problem called the diamond problem. The name reflects the shape of the inheritance diagram

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

# There is the highest superclass called A;
#     There are two subclasses derived from A: B and C;
#     and there is also the lowest subclass called D, derived from B and C (or C and B, as these two variants mean
#     different things in Python)
#
# Can you see the diamond there?

# Some programming languages prohibit multiple inheritance, and as a consequence, don't let you build a diamond - this
# is the route that Java and C# have chosen to follow since their origins.
#
# Python, however, has chosen a different route - it allows multiple inheritance, and doesn't care if you write and
# execute code like what's in the editor. But don't forget the MRO - he's always in charge.
#
# Let's reconstruct our example from the previous page to make it more like a diamond, like below:

class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Note: both Middle classes define a method with the same name: m_middle().
#
# It introduces a little uncertainty into our sample, although we are absolutely certain it can answer the following
# key question: which of the two m_middle() methods will actually be invoked when the following line is executed?
#
# Object.m_middle()
#
# In other words, what will you see on the screen: middle_left or middle_right?
#
# No need to rush - think twice and keep Python MRO in mind!
#
# Are you ready?
#
# Yes, you're right. The invocation will activate the m_middle() method, which comes from the Middle_Left class.
# The explanation is simple: the class is listed before Middle_Right in the inheritance list of the Bottom class. If you want to make sure there are no doubts, try swapping these two classes in the list and check the results.
#
# If you want to experience some deeper impressions about multiple inheritance and gems, try modifying our snippet
# and equipping the Upper class with another specimen of the m_middle() method, and carefully investigate its behavior.
#
# As you can see, diamonds can bring some problems into your life - both the real ones and those offered by Python.
