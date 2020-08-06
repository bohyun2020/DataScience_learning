from csv import reader


"""
2. Opening and Exploring the Data
"""
"""
### The Google Play data set ###
opened_file = open('googleplaystore.csv', encoding='utf-8')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]



### The App Store data set ###
opened_file = open('AppleStore.csv', encoding='utf-8')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
print(android_header)
print('\n')
explore_data(android, 1, 3, True)

print(ios_header)
print('\n')
explore_data(ios, 1, 3, True)
"""
"""
3. Deleting Wrong Data
    1) Detect inaccurate data, and correct or remove it.
    2) Detect duplicate data, and remove the duplicates.

"""
"""

# 4. Removing Duplicate Entries: Part One 

### The Google Play data set ###
opened_file = open('googleplaystore.csv', encoding='utf-8')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('AppleStore.csv', encoding='utf-8')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(len(android))
del android[10472]
print(len(android))

"""
"""
Created two lists: 

1) one for storing the name of duplicate apps. 
2) and one for storing the name of unique apps.


"""
"""
opened_file = open('googleplaystore.csv', encoding='utf-8')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

opened_file = open('AppleStore.csv', encoding='utf-8')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(len(android))
del android[10472]
print(len(android))

# 1) 얼마만큼 중복되는 지 보기 위해서, 아래 empty list를 만들어서 비교하였고,
#       총 10840 row 중 9659(1181 중복 row을 파악함)

duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)

print(len(android))
print(len(unique_apps))
print(len(duplicate_apps))

print('Expected length: ', len(android) - len(duplicate_apps))


# 2) Empty dict를 이용해서 name과 최고 review 값 파악. 

max_reviews = {}
for app in android:
    name = app[0]
    n_reviews = float(app[3])                                                   # 중요: 숫자는 float 함수 쓰는걸 기억

    if name in max_reviews and n_reviews > max_reviews[name]:
        max_reviews[name] = n_reviews                                           # 중요: Dict는 append가 없다. 
    elif name not in max_reviews:
        max_reviews[name] = n_reviews

print(len(max_reviews))

# 3) 2개의 empty list를 만들어서 
#       1. list에 app data 나열 ( review 값은 최고값 적용 -> 총 개수 9659)
#       2. list에 name 값 나열 ( 총 개수 9659)

android_clean = [] # which will store our new cleaned data set
already_added = [] # which will just store app names

for app in android:
    name = app[0]
    n_reviews = float(app[3])

    if max_reviews[name] == n_reviews and name not in already_added:
        android_clean.append(app)
        already_added.append(name)

print(len(android_clean))
print(len(already_added))



"""
"""
6. Removing Non-English Apps: Part One

    The numbers corresponding to the characters we commonly use in an English 
    text are all in the range 0 to 127, according to the ASCII (American Standard 
    Code for Information Interchange) system.

    If an app name contains a character that is greater than 127, 
    then it probably means that the app has a non-English name.
"""
"""
# 1. Example

print(ord('A'))
print(ord('a'))
print(ord('`'))
print(ord('/'))
print(ord('='))
print(ord('+'))
print(ord('@'))
print(ord('ㄱ'))
print(ord('你'))

string = '你ㄱㄷ'
for character in string:
    print(ord(character))
"""
"""
# 2. Exercise

def is_english(string):

    for character in string:
        if ord(character) <= 127:
            return True

        return False

print(is_english('instagram')) 
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(is_english('😜'))
"""
"""
7. Removing Non-English Apps: Part Two
     To minimize the impact of data loss, we'll only remove an app if its name 
     has more than three characters with corresponding numbers falling outside 
     the ASCII range.

     This means all English apps with up to three emoji or other special 
     characters will still be labeled as English. Our filter function is still 
     not perfect, but it should be fairly effective.
"""
"""
def is_english(string):                                                         # 중요 꼭 기억하기 
    non_ascii = 0

    for character in string:
        if ord(character) > 127:
            non_ascii += 1

    if non_ascii > 3:
        return False

    return True
            
print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
"""
"""
    Change the function you created in the previous screen. If the input string 
    has more than three characters that fall outside the ASCII range (0 - 127), 
    then the function should return False (identify the string as non-English), 
    otherwise it should return True.
"""
"""
android_english = []                                                             # 방법 중요 꼭 알기
for app in android:
    name = app[0]
    if is_english(name):
        android_english.append(app)

ios_english = []
for app in ios:
    name = app[0]
    if is_english(name):
        ios_english.append(app)

explore_data(android_english, 1, 3, True)
explore_data(ios_english, 1, 3, True)
"""
"""
10. Most Common Apps by Genre: Part Two
    we'll need to make use of the built-in sorted() function. 
    This function takes in an iterable data type (like a list, dictionary, 
    tuple, etc.), and returns a list of the elements of that iterable sorted 
    in ascending or descending order (the reverse parameter controls 
    whether the order is ascending or descending).
"""
"""
# 1) Sorting a list Temporarily with the sorted() Function
a_list = [50, 20, 100]
print(sorted(a_list))
print(sorted(a_list, reverse=True))


# 2) Sorting a list Permanently with the sort() Method.
b_list = [20, 10, 300]
b_list.sort()
print(b_list)

# 3) Printing a list in Reverse Order
c_list = [80, 10, 200]
c_list.reverse()
print(c_list)

"""
"""
    # 4) The sorted() function doesn't work too well with dictionaries because 
        it only considers and returns the dictionary keys.

        However, the sorted() function works well if we transform the dictionary
        into a list of tuples. 
        the dictionary value comes first, and the dictionary key comes second:
"""
"""

freq_table = {'Genre_1' : 50, 'Genre_3' : 20, 'Genre_2' : 100}
print(sorted(freq_table))

freq_table_as_tuple = [(50, 'Genre_1'), (20, 'Genre_3'), (100, 'Genre_2')]
print(sorted(freq_table_as_tuple))

"""
"""
This is a bit overcomplicated to just sort a dictionary, but there are much 
simpler ways to do this once we learn more advanced techniques. 
Using the workaround above, we wrote a helper function for you named display_table()
"""

def freq_table(dataset, index):                                                     
    table = {}
    total = 0

    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1

    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[value] = percentage

    return table_percentages

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse=True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


def freq_table(dataset, index):                                                 # 중요: 다시 공부하기
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
