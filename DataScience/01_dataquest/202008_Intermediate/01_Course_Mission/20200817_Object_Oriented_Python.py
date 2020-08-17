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



