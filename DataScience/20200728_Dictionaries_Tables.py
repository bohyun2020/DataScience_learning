# Dictionaries And Frequency Tables
# 1.Storing Data

# Content rating  Number of apps
# 4+  4,433
# 9+  987
# 12+ 1,155
# 17+ 622

# List 2개를 합쳐서 Dictionary로 만들어서 표현
"""
content_ratings = ['4+', '+9', '+12', '+17']
numbers = [4433, 987, 1155, 622]
content_ratings_numbers = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622} # index:value pattern

print(content_ratings_numbers)

over_9 = content_ratings_numbers['9+']
over_17 = content_ratings_numbers['17+']

print(over_9)
print(over_17)

"""
"""
With dictionaries, there's no longer a connection between the index of a value 
and the position of that value in the dictionary

"""
# dictionary_name[index] = value
"""
content_ratings = {}
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']
print(content_ratings)
print(over_12_n_apps)
"""

"""

# 1. Dictionary keys can be of almost any data type we've learned so far, except lists and dictionaries.
# 2. Dictionary values can be of any data type: strings, integers, floats, Booleans, lists, and even dictionaries.


d_1 = { 'key_1' : 'value_1',            # Strings
        'key_2' : 1,                    # Integer
        'key_3' : 1.832,                # Float
        'key_4' : False,                # Booleans                                       
        'key_5' : [1, 2, 3],            # Lists
        'key_6' : {'inner_key' : 10}    # Dictionaries
      }

print(d_1)

"""
"""
# 1. If we use lists or dictionaries as dictionary keys, the computer raises an error:
# 
# 왜냐하면
# When we populate a dictionary, Python tries to convert each dictionary key to 
# an integer (even if the key is of a data type other than an integer) in the background.
# the hash() command doesn't transform lists and dictionaries to integers, and returns an error instead.

d_2 = { [1, 2, 3] : 'list'}
d_3 = { {'key' : 'value'} : 'dictionary'}

print(d_2)
print(d_3)

"""

"""

# 2. When we populate a dictionary, we also need to make sure each key in that dictionary is unique.

d_1 = { 'a_key' : 1,
        'a_key' : 2 }
print(d_1)

"""

"""
# 3. The hash() command converts the Boolean True to 1, and the Boolean False to 0
# This means the Booleans True and False will conflict with the integers 0 and 1.
# The dictionary keys won't be unique anymore, and 
# Python will only keep the last key-value pair in cases like that.

d_1 = {1 : 'one', True : 'Boolean'}
d_2 = {False : 'Bool', 0 : 'Zero'}
d_3 = {0 : 'Zero', 1 : 'one', 2 : 'two', True : 'true', False : 'false'}

print(d_1)
print(d_2)
print(d_3)

d_1 = {'key_1': 'first_value', 
       'key_2': 2,
       'key_3': 3.14,
       'key_4': True,
       'key_5': [4,2,1],
       'key_6': {'inner_key' : 6}
      }

print(d_1)
"""

"""
# How did we find out there are 4,433 apps with a 4+ content rating, or 622 apps with a 17+ rating?
# 1. List로 심심해서 풀어봤쪄 
# 1번째 방법

opened_file = open('AppleStore.csv', encoding = 'UTF-8')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

n_apps = 0
for row in apps_data[1:]:
    cont_rating = row[10]
    if cont_rating == '4+':
        n_apps += 1

print(n_apps)

# 2번째 방법

opened_file = open('AppleStore.csv', encoding = 'UTF-8')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

n_apps = []
for row in apps_data[1:]:
    cont_rating = row[10]
    user_id = row[0]
    if cont_rating == '4+':
        n_apps.append(user_id)

print(len(n_apps))
"""

"""
# Once we've created a dictionary, we can check whether a certain value exists in the dictionary
# To do that, we use the in operator.
# If we use in with a certain value that doesn't exist among a dictionary's keys, False is returned.

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print('12+' in content_ratings)
is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings 

# value를 검색하면 항상 False로 나옴 
# because the search is done only over the dictionary's keys

print(is_in_dictionary_1)    # is_in 이런식으로 variable name 짓는 거 기억하기
print(is_in_dictionary_2)

if '17+' in content_ratings:
    result = "It exists"
    print(result)

"""

"""
# 7. Counting with Dictionaries

content_ratings = {'4+' : 4433, '9+' : 987, '12+' : 1155, '17+' : 622}

content_ratings['4+'] = 0
content_ratings['9+'] += 13
content_ratings['12+'] -= 1155
content_ratings['17+'] = '622'

print(content_ratings)
"""
"""
# 1. 예제로 푸는 Counting
# because the search is done only over the dictionary's keys
# value를 검색하면 항상 False로 나옴 

content_ratings = {'4+' : 0, '9+' : 0, '12+' : 0, '17+' : 0}
ratings = ['4+', '4+', '4+', '9+', '12+', '17+']

for c_rating in ratings:                 # 첫 번째, 리스트 for loop 써서 정리 
    if c_rating in content_ratings:      # 두 번째, '4+'이 content_ratings에 있는 지 비교
        content_ratings[c_rating] += 1      # 있다면, value에 +1을 해주기

print(content_ratings)
"""

# 2. 실전 Excel Counting 
"""
opened_file = open('AppleStore.csv', encoding = 'UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+' : 0, '9+' : 0, '12+' : 0, '17+' : 0}

for row in apps_data[1:]:
    count_rating = row[10]
    if count_rating in content_ratings:
        content_ratings[count_rating] += 1

print(content_ratings)
"""

# 8. Finding the Unique Values
# Previously, we created the dictionary {'4+': 0, '9+': 0, '12+': 0, '17+': 0} 
# before we looped over the data set to count the occurrence of each content rating. 
# Unfortunately, this approach requires us to know beforehand the unique values we want to count.

# 1) 예제 문제  **중요**
"""
content_ratings = {}
ratings = ['4+', '4+', '4+', '9+', '12+', '17+']

for c_rating in ratings:
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1

print(content_ratings)
"""
"""
# 2) 연습문제 **중요**
opened_file = open('AppleStore.csv', encoding = 'UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}
for row in apps_data[1:]:
    cont_rating = row[10]
    if cont_rating in content_ratings:
        content_ratings[cont_rating] += 1
    else:
        content_ratings[cont_rating] = 1

print(content_ratings)
"""
"""
# 3) 연습문제 **중요**
opened_file = open('AppleStore.csv', encoding = 'UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}
for row in apps_data[1:]:
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1

print(genre_counting)
"""

# 10. Looping over Dictionaries
# To transform frequencies to proportions or percentages, we can update 
# the dictionary values individually by performing the required arithmetical operations.

"""
# 1) Proportion
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for iteration_variable in content_ratings:
    content_ratings[iteration_variable] /= total_number_of_apps

print(content_ratings)
"""
"""
# 2) Percentage
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for iteration_variable in content_ratings:
    content_ratings[iteration_variable] /= total_number_of_apps
    content_ratings[iteration_variable] *= 100                                   #이거 잘 기억해두기 percentage로

percentage_17 = content_ratings['17+'] 
percentage_15_allowed = 100 - percentage_17

print(percentage_17)
print(percentage_15_allowed)
"""

"""
# we'll often need to keep the dictionaries separate for later analysis.
# For instance, we might want to have three separate dictionaries: 
# one storing frequencies, another storing proportions, and another storing percentages.

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_proportions = {}
c_ratings_percentage = {}

for key in content_ratings:                                                     # 새로운 dict에 proportion과 
    proportion = content_ratings[key] / total_number_of_apps                    # perntage 를 각각 집어 넣기 
    c_ratings_proportions[key] = proportion
    c_ratings_percentage[key] = proportion * 100

print(c_ratings_proportions)
print(c_ratings_percentage)
"""

"""
# 12. Frequency Tables for Numerical Columns
    # Creating frequency tables for certain columns may result in creating lengthy dictionaries

opened_file = open('AppleStore.csv', encoding ='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

size_freq = {}
for row in apps_data[1:]:
    size = row[2]
    if size in size_freq:
        size_freq[size] += 1
    else:
        size_freq[size] = 1

print(len(size_freq))
print(size_freq)

"""

"""
    # A lengthy frequency table is difficult to analyze. 
    # The lengthier the table, the harder it becomes to see any patterns. 
    # Using intervals helps us segment the data into groups, which eases analysis

    # When we're trying to come up with some reasonable intervals, 
    # it often helps to know the minimum and the maximum values of a column


opened_file = open('AppleStore.csv', encoding ='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for row in apps_data[1:]:
    size = float(row[2])
    data_sizes.append(size)

print(min(data_sizes))
print(max(data_sizes))

# 왜 dict로 안했지? / dict으로 하는 방법도 생각해보자 
"""

# 13. Filtering for the Intervals
"""
opened_file = open('AppleStore.csv', encoding ='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = {'0 - 10 MB': 0, '10 - 50 MB': 0, '50 - 100 MB': 0, 
              '100 - 500 MB': 0, '500 MB +': 0}

for row in apps_data[1:]:
    data_size = float(row[2])
    
    if data_size < 1000000:
        data_sizes['0 - 10 MB'] += 1

    elif 1000000 <= data_size < 50000000:
        data_sizes['10 - 50 MB'] += 1

    elif 50000000 <= data_size < 100000000:
        data_sizes['50 - 100 MB'] += 1

    elif 100000000 <= data_size < 500000000:
        data_sizes['100 - 500 MB'] += 1

    elif 500000000 <= data_size:
        data_sizes['500 MB +'] += 1
"""

# 연습문제 

opened_file = open('AppleStore.csv', encoding ='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
for row in apps_data[1:]:
    rating_count_tot = float(row[5])
    ratings.append(rating_count_tot)

print(min(ratings))
print(max(ratings))

data_sizes = {'0 - 50k': 0, '50k - 100k': 0, '100k - 500k': 0, '500k - 1000k': 0}
for row in apps_data[1:]:
    rating_count_tot = float(row[5])

    if 0 <= rating_count_tot < 50000:
        data_sizes['0 - 50k'] += 1

    elif 50000 <= rating_count_tot < 100000:
        data_sizes['50k - 100k'] += 1

    elif 100000 <= rating_count_tot < 500000:
        data_sizes['100k - 500k'] += 1

    elif 500000 <= rating_count_tot < 1000000:
        data_sizes['500k - 1000k'] += 1

print(data_sizes)