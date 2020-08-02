# 1. Functions
"""
    It takes in an input.
    It does something to that input.
    It gives back an output.

    we could use what we've learned to write code that manages to perform 
    the same task as len() does. This should give us some insight into 
    how the len() function counts the length of a list
"""
"""
# 1) Length Fucntion을 사용하지 않고, 코드로 계산한 방법
a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

length = 0
for element in a_list:
    length += 1
print(length)
"""
"""
# 2) Let's now try to guess how the sum() function might work behind the scenes.

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

number_sum = 0
for element in a_list:
    number_sum += element

print(number_sum)
print(sum(a_list))
"""
"""
# 2. Built-in Functions

    We've seen that Python has a couple of ready-made functions like 
    sum(), len(), min(), and max(). These functions are already built into Python 
    and are available for immediate use. Because they are already built-in, 
    they are called built-in functions

    Python doesn't have a built-in function to accomplish this. 
    However, Python allows us to write our own functions, which means we can 
    create a function that generates frequency tables.

    Starting with the next screen, we'll discuss the details around creating 
    functions. For now, let's remind ourselves the workflow for generating a 
    frequency table by doing the exercises below.
"""
"""
ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}

for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
print(content_ratings)

"""
"""
# 3. Creating Our Own Functions

    On the previous screen, we mentioned that our goal is to create a function that 
    generates a frequency table. This process, however, is a bit more complex, 
    so we'll start with more simple examples and build up from there toward that goal.
"""
"""
def square(a_number):
    squared_number = a_number * a_number
    return squared_number

square_6 = square(6)
print(squared_6)

def greet_user(username):
    return f"Hello, {username.title()}"

greet_bohyun = greet_user('Bohyun')
print(greet_bohyun)

"""
"""
# 4. The Structure of a Function

    Structurally, the function above is composed of a header (which contains 
    the def statement), a body, and a return statement. Together, these three 
    elements make up the function's definition. We'll often use the phrase "inside
    the function's definition" to refer to the function's body.
"""
"""
def add_10(number):               # Header 
    result = number + 10          # Body
    return result                 # the return statement

add_30 = add_10(number=30)
add_90 = add_10(number=90)
print(add_30)
print(add_90)
"""
"""
# 5. Parameters and Arguments
    you can couple the return statement with an entire expression rather 
    than just a single variable. This means we can directly return the result 
    of the expression a_number * a_number and omit the variable assignment step
"""
"""
def square(a_number):
    square = a_number * a_number
    return square
print(square(6))
"""
"""
    Skipping a variable assignment step or two to simplify our code is generally a good idea
"""
"""
def square(a_number):
    return a_number * a_number

print(square(6))
"""
"""
# 6. Extract Values From Any Column

    creating a function that generates frequency tables for any column we want   # 완전 중요
    in our iOS apps data set.
    완 전 중 요 
"""
"""
opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
    return column

cont_rating = extract(10)
print(cont_rating)
"""
"""
# 7. Creating Frequency Tables
    we'll create the second function. Remember that to create a frequency table 
    for the elements of a list, we need to:

    Write a function named freq_table() that generates a frequency table for any list.
"""
"""
# 1) 아래 예제를 풀어야지 Funtion 설정이 이해가 간다. 
ratings = ['4+', '4+', '4+' , '9+', '9+', '12+', '17+']
content_ratings = {}

for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1

print(content_ratings)

"""
"""
# 2) 실전 Function을 이용한 자동화 응용 
    Feel free to experiment with the extract() and freq_table() functions 
    to easily create frequency tables for any column you want.

    extract() -> column list 만들고
    freq_table() -> column list를 활용해서 freq_table() dictionary 완성

"""
"""
opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):                                                              # 완전 중요 
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
    return column

def freq_table(column):
    frequency_table = {}
    for element in column:
        if element in frequency_table:
            frequency_table[element] += 1
        else:
            frequency_table[element] = 1
    return frequency_table

genres = extract(10)
genres_ft = freq_table(genres)
print(genres_ft)

"""
"""
# 8. Writing a Single Function
    we can write a single function to generate the frequency tables 
    for any column we want. Let's try that in the following exercise.

    # 1번쨰 방법 column list(append) -> dictionary 로 연결 (2단계로 나뉘어짐. 단점) # 중요
    # 2번째 방법 dict(variable[index] = value)로 바로 연결 
        if statement -> True +=1 , False = 1 (1단계로 끝낼 수 있음)
"""
"""
opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(index):
    frequency_table = {}

    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1

    return frequency_table

genre_ft = freq_table(11)
print(genre_ft)
"""
"""
# 9. Reusability and Multiple Parameters
    One of the key aspects that make functions great is reusability.    
    We need to enlarge its degree of reusability by making it reusable with 
    respect to both columns and data set

    To do that, we'd need to change our function to not only take an index value 
    as the input, but also a data set. So instead of having freq_table(index), 
    we'd need something like freq_table(index, data_set)
"""
"""
opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(apps_data, 7)
print(ratings_ft)

"""
"""
# 10. Keyword and Positional Arguments
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set=apps_data, index=7)
genres_ft = freq_table(index=11, data_set=apps_data)

"""
"""
# 11. Combining Functions
    When we write a function, it's common to use other functions inside 
    the body of the function we're creating.
"""
"""
# 1) 예제
def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += element
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1 
    return length

def mean(a_list_of_numbers):
    sum_list = find_sum(a_list_of_numbers)
    len_list = find_length(a_list_of_numbers)
    mean_list = sum_list / len_list

    return mean_list

list_1 = [5, 10, 15]
print(mean(list_1))
"""

# 2) Reusing functions inside other functions enables us to elegantly build 
#    complex functions by abstracting away function definitions:
"""
def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += element
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1 
    return length

def mean(a_list_of_numbers):
    return find_sum(a_list_of_numbers) / find_length(a_list_of_numbers)

print(mean([5, 10, 15]))
"""
"""
# 연습문제
    # Write a function named mean() that computes the mean for any column we want from a data set.

opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):                                                      # 중요! 연습 더 해야함.
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
print(avg_price)
"""
