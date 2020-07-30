"""
# 1. Interfering with the Built-in Functions
    Run the code del max to delete the max() function you wrote.
    This will allow you to use the built-in max() function again.
"""
"""
a_list = [1, 8, 10, 9, 7]
print(max(a_list))

def max(a_list):
    return "No max value returned"

max_val_test_0 = max(a_list)
print(max_val_test_0)

del max

print(max(a_list))
"""
"""
# 2. Variable Names and Built-in Functions
    'int' object is not callable
"""
"""
sum = 5 + 12
list_1 = [5, 10, 15]
sum(list_1)             # 17(list_1) The integer 17 can't be called like a function
                        # hence the error message 'int' object is not callable.

"""
"""
# 3. Default Arguments
    When we create a function, we can initiate parameters with certain default values 
    — we call these values default arguments.

    Default arguments are not set in stone,                                     ** Important ** 
    and can be easily modified when we call a function:
"""
"""
def add_value(x, constant=10):
    return x + constant

print(add_value(3))
print(add_value(3, constant=50))
"""
"""
    If all parameters have default arguments, it then becomes possible 
    to call a function without passing in any argument:

    Default arguments come in handy when we anticipate that we'll use an 
    argument frequently — this can save us some time when we reuse the functions. 
    Default arguments are also very useful for building complex functions

"""
"""
def add_value(x=9, constant=10):
    return x + constant

print(add_value(3))
"""
"""
# Exercise
    Let's now build a function that opens a CSV file and makes use of default 
    arguments at the same time.
"""
"""
def open_dataset(file_name='AppleStore.csv'):

    opened_file = open(file_name, encoding='UTF-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    return data

apps_data = open_dataset()
print(apps_data[1:6])
"""
"""
# 4. The Official Python Documentation
    Open() function
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
    closefd=True, opener=None)

    With the exception of the file parameter, we can see that all parameters 
    have default arguments. This means the only argument we must pass in is 
    for the file parameter.

    This example shows us how useful default arguments really are. 
    With the help of default arguments, we can use a complex function like 
    open() only by passing the file name. If open() didn't have any default 
    argument, then we'd have to pass in arguments for all the parameters.

"""
"""
    Python 3.8.5 documentation
    https://docs.python.org/3/
"""
"""
# 5. Multiple Return Statements
    it's possible to use multiple return statements.
    Combining return with an if statement and an else clause, we can implement 
    the ability to specify whether we want a sum or a difference returned:
"""
"""
# 1) Example
def sum_or_difference(a, b):
    a_sum = a + b
    difference = a - b
    return ?
"""
"""
def sum_or_difference(a, b, do_sum=True):
    if do_sum:
        return a + b
    else:
        return a - b

print(sum_or_difference(10, 5, do_sum=True))
print(sum_or_difference(10, 5, do_sum=False))
"""
"""
    Note that there's more than one way to make the sum_or_difference() function 
    work as we want it to. Below, we redefine the function without using 
    an else clause:
"""
"""
# 2) Example
def sum_or_difference(a, b, do_sum=True):
    if do_sum:
        return a + b
    
    return a - b

print(sum_or_difference(10, 5, do_sum=True))
print(sum_or_difference(10, 5, do_sum=False))
"""
"""
# 3) Exercise
    If the parameter indicates that data set has a header row, 
    the function removes the header row before returning the data set.
"""
"""
def open_dataset(file_name='AppleStore.csv', header=True):

    opened_file = open(file_name, encoding='UTF-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:]
    else:
        return data

apps_data = open_dataset()
print(apps_data)
"""
"""
# 6.Returning Multiple Variables
    Python allows us to build functions that return more than just one variable. 
    This means that we can create a function that returns both a sum and a difference.
"""
"""
    # 1) example

def sum_and_difference(a, b):
    a_sum = a + b
    difference = a - b 
    return a_sum, difference

sum_diff = sum_and_difference(10, 5)
print(sum_diff)
type(sum_diff)
"""
"""
    One thing you might find a bit odd is the structure of the output (20, 10). 
    (20, 10) is a tuple, which is a data type that is very similar to a list 
    (recall that examples of data types include integers, strings, lists, dictionaries, etc.).
"""
"""
    The main difference between tuples and lists boils down to whether we can 
    modify the existing values or not. In the case of tuples, we can't modify 
    the existing values, while in the case of lists, we can. Below, we're trying
    to modify the first value of a list and a tuple.
"""
"""
a_list = [1, 'a', 10.5]
a_list[0] = 99
print(a_list)
"""
"""
a_list = [1, 'a', 10.5]
a_tuple = (1, 'a', 10.5)

print(a_tuple[0])
print(a_list[0])
print(a_tuple[-1])
print(a_list[-1])

"""
"""
    # 2) example 

    TypeError: 'tuple' object does not support item assignment

    Tuples are called immutable data types because we can't change their state 
    after they've been created
"""
"""
a_tuple = (1, 'a', 10.5)
a_tuple[0] = 99
print(a_tuple)
"""
"""
    # 3) exercise
    If the data set has a header, the function returns separately 
    both the header and the rest of the data set.

"""
"""
def open_dataset(file_name='AppleStore.csv', header=True):

    opened_file = open(file_name, encoding='UTF-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:
        return data[0], data[1:]

    else:
        return data

all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

print(header)
print(apps_data)
"""
"""
# 7. More About Tuples
    1) When we create a tuple, surrounding the values with parentheses is optional
"""
"""
a_tuple = (1, 'a')
print(a_tuple)
print(type(a_tuple))

a_tuple = 1, 'a'
print(a_tuple)
print(type(a_tuple))
"""
"""
    # 2) With this in mind, remember the syntax we used in the return statement 
    #    to return multiple values:

def sum_and_difference(a, b):
    a_sum = a + b
    difference = a - b
    return a_sum, difference

sum_diff = sum_and_difference(15, 5)
print(sum_diff)
"""
"""
    # When we work with tuples, we can assign their individual elements 
    # to separate variables in a single line of code.

a_tuple = 1, 2
first_element = a_tuple[0]
second_element = a_tuple[1]

print(first_element)
print(second_element)

a_tuple = 1, 2
first_element, second_element = a_tuple

print(first_element)
print(second_element)

    # We can do the same with lists — we can assign individual list elements 
    # to separate variables in a single line of code:

a_list = [1, 2]
first_element = a_list[0]
second_element = a_list[1]

print(first_element)
print(second_element)

a_list = [1, 2]
first_element, second_element = a_list

print(first_element)
print(second_element)
"""
"""
    # We can use this variable assignment technique with functions that return multiple variables.

def sum_and_difference(a, b):
    a_sum = a + b
    difference = a - b
    return a_sum, difference

a_sum, a_diff = sum_and_difference(15, 5)
print(a_sum)
print(a_diff)
"""
"""
# Exercise
    * Do the variable assignment step in a single line of code.
        1) Assign the header to a variable named header.
        2) Assign the rest of the data set to a variable named apps_data.
"""
"""
def open_dataset(file_name='AppleStore.csv', header=True):

    opened_file = open(file_name, encoding='UTF-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:
        return data[0], data[1:]

    else:
        return data

header, apps_data = open_dataset()
"""
"""
# 8. Functions — Code Running Quirks
    Functions without a return statement don't return any value. However, 
    strictly speaking, they return a None value, which practically represents 
    the absence of a value.

     The None value is an instance of the NoneType data type 
     (just like 5.321 is an instance of the float data type).
"""
"""
def print_constant():
    x = 3.14
    print(x)

j = print_constant()
print(j)
print(type(j))
"""
"""
# 9. Scopes — Global and Local
    the quirk is that Python only saves the x variable temporarily. Python saves
    x into a kind of temporary memory, which is immediately erased after 
    the print_constant() finishes running.

    This kind of temporary memory storage doesn't apply to the code that is being 
    run outside function definitions. If we define x = 3.14 in our main program 
    (outside function definitions), we can use x later on without having to 
    worry that it was erased from memory.

    The part of a program where a variable can be accessed is often called scope. # Global Scope
    The variables defined in the main program are said to be in the global scope, # Local Scope
    while the variables defined inside a function are in the local scope.

"""
"""
e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e**x

result = exponential(5)
print(e)
print(result)

"""
"""
e = 'mathematical constant'                                                     # 중요! Error 발생 or not?
a_sum = 1000
length = 50

def divide():
    print(a_sum)
    print(length)
    return a_sum / length

result_2 = divide()
print(result_2)
"""
"""
# 10. Scopes — Searching Order
Python searches the global scope if a variable is not available in the local 
scope, but the reverse doesn't apply — Python won't search the local scope 
if it doesn't find a variable in the global scope. Even if it searched the local 
scope, remember the memory associated with a function is temporary, 
so the search would be pointless. Recall that we've already seen this effect 
(Python not searching the local scope) in one of the code examples of 
the previous screen:

"""