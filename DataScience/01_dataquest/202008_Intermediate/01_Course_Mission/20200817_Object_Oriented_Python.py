"""

# 1. Introduction
object-oriented programming (OOP). Rather than code being designed 
around sequential steps, it is instead defined around objects.


    1) An object is an entity that stores data.
    2) An object's class defines specific properties objects of that class will have.

        object similar variable
        class similar type

"""
"""
# Exercise

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

print(type(1))
print(type(s))
print(type(d))
"""
"""

# 3. Defining a Class
    1) Snake Case - like_this
    2) Pascal Case  - LikeThis

"""
"""
# Sample

class NewList():
    pass

"""
"""

# 4. Instantiating a Class

# (4.1) Tesla Red and Blue car
    # 1) These cars are two instances of the Tesla class
    # 2) While each is unique - for example, one is red and one is blue - 
        # they are clearly the same type of car.


string_1 = "The first string"
string_2 = "The second string"

# (4.1) String_1 and String_2 
    # 1) These objects are two instances of the Python str class.
    # 2) While each is unique - they contain unique value - They are the same type of object.


# (4.3) Institation
    : Once we have defined our class, we can create an object of that class,
      which is known as instantiation.

    my_class_instance = MyClass()

    - Instantiated an object of the class MyClass.
    - Assigned that instance to the variable named my_class_instance.

"""
"""
# Exercise 

class NewList():
    pass

newlist_1 = NewList()
print(type(newlist_1))

"""
"""
# 5. Creating Methods

In order to make our class do something, we need to define some methods
Methods allow objects to perform actions.

"""
"""
# 1) Sample

my_string = "hello"   # an object of the str class
my_list = [1, 2, 3]   # an object of the list class

my_list.append(4)
print(my_list)

my_string = my_string.replace("h", "H")
print(my_string)

my_string.append("!")

"""
"""
# 2 ) Exercise

class NewList(DQ):
    
    def first_method():
        return "This is my first method."
    
newlist = NewList()

"""
"""
# 6. Understanding 'self'

class NewList():

    def first_method(self):
        print("hello")

instance = NewList()
instance.first_method()
"""
"""
# TypeError: first_method() takes 0 positional arguments but 1 was given        # 이해하는 거 중요합니다. 

* It says that one argument was given to first_method(), but when we called 
the method we didn't provide any arguments. It seems like there is a "phantom" 
argument being inserted somewhere. 


"""
"""
# 1) Sample
# create a str object
s = "MY STRING"

# call `str.title() directly
# instead of `s.title()`
result = str.title(s)
print(result)
"""
"""
# 2) Sample
class MyClass():
    def print_self(self):
        print(self)

mc = MyClass()
mc.print_self()
"""
"""
# 3) Exercise

class NewList():

    def first_method(self):
        return "This is my first method"

newlist = NewList()
result = newlist.first_method()
"""
"""
# 7. Creating a Method That Accepts an Argument

"""
"""
# 1) Sample
class MyClass():
    def return_string(self, string):
        return string

mc = MyClass()
result = mc.return_string("Hey there!")
print(result)
"""
"""
2) Exercise
class NewList(DQ):
    
    def return_list(self, input_list):
        return input_list
  
newlist = NewList()
result = newlist.return_list([1, 2, 3])
"""
"""
# 8. Attributes and the Init Method

The power of objects is in their ability to store data, 
and data is stored inside objects using attributes.

Relating back to our Tesla metaphor, an object of the Tesla "class" has 
attributes like their color, battery, and motor.

You can think of attributes like special variables that belong to a particular class.

We define what is done with any arguments provided at instantiation using the init method.
The init method — also called a constructor 

The init method's most common usage is to store data as an attribute:

"""
"""
# 1) Sample
class MyClass():
    def __init__(self, string):
        print(string)

mc = MyClass("Holla")
"""
"""
# 2) Sample

class MyClass():
    def __init__(self, string):
        self.my_attribute = string  # string = "Hola!"

    def study_hard(self, name):
        name = name.title()
        msg = "{}! Welcome to our studying place".format(name)
        return msg 


mc = MyClass("Hola!") # now we have stored "Hola" in the attribute my_attribute inside our object.
print(mc.my_attribute) # Like methods, attributes are accessed using dot notation, 
                       #    but attributes don't have parentheses like methods do. 
print(mc.study_hard("bohyun"))
"""
"""
Let's take a moment to summarize what we've learned so far:

1) The power of objects is in their ability to store data.
2) Data is stored as attributes inside objects.
3) We access attributes using dot notation.
    To give attributes values when we instantiate objects, 
4) we pass them as arguments to a special method called __init__(), 
    which runs when we instantiate an object.
"""
"""
# 3) Exercise
class NewList():

    def __init__(self, initial_state):
        self.data = initial_state
        
my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)
"""
"""
# 9. Creating an Append Method

"""
"""
# 1) Sample
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)

my_list = [1, 2, 3]
new_item = 4
new_item_list = [new_item]  
my_list = my_list + new_item_list
print(my_list)

"""
"""
# class NewList():

#     def __init__(self, new_list):
#         self.data = new_list

#     def append(self, add_value):
#         all_list = self.data + [add_value]
#         return all_list

# list1 = NewList([1, 2, 3, 4])
# print(list1.append(5))

class NewList():
   
    def __init__(self, initial_state):
        self.data = initial_state

    def append(self, new_item):
        self.data += [new_item]

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)

my_list.append(6)
print(my_list.data)

"""
"""
# 10. Creating and Updating an Attribute

class NewList():
   
    def __init__(self, initial_state):
        self.data = initial_state
        self.cal_length()

    def cal_length(self):
        length = 0
        for item in self.data:
            length += 1
        self.length = length

    def append(self, new_item):
        self.data += [new_item]
        self.cal_length()


my_list = NewList([1, 2, 3, 4, 5])
print(my_list.length)

my_list.append(6)
print(my_list.length)
"""
"""

Rather than writing the code out twice, we can add a helper method, 
which calculates the length, and just call that method in the appropriate places.

"""

class MyBankBalance():

    def __init__(self, total_amount):
        self.bank_balance = total_amount
        self.string_format()

    def string_format(self):
        self.balance_format = "$ {:,.2f}".format(self.bank_balance) 


    def add_value(self, value):
        self.bank_balance += value
        self.string_format()

balance = MyBankBalance(300)
print(balance.balance_format)


# 1) Sample
class MyBankBalance():
    # An object that tracks a bank account balance

    def __init__(self, inital_balance):
        self.balance = inital_balance
        self.cacl_string()

    def cacl_string(self):
        # A helper method to update self.string
        string_balance = "${:,.2f}".format(self.balance)
        self.string = string_balance

    def add_value(self, value):
        # Add value to the bank balance 
        self.balance += value
        self.cacl_string()

mbb = MyBankBalance(3.50)
print(mbb.string)

mbb.add_value(5000)
print(mbb.string)

"""
class NewList():
  
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    
    def calc_length(self):
    
        length = 0
        for item in self.data:
            length += 1
        self.length = length
    
    def append(self, new_item):

        self.data = self.data + [new_item]
        self.calc_length()

fibonacci = NewList([1, 1, 2, 3, 5])
print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)
"""
"""
ex = "1, 2, 3,,4,"
ex = ex.split(",", maxsplit=1)
print(ex)
"""
