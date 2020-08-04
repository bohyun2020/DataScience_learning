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




# 4. Removing Duplicate Entries: Part One 
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

print(len(android))
del android[10472]
print(len(android))


duplicates_apps = []
unique_apps = []
for app in android:
    name = app[0]
    if name in unique_apps:
        duplicates_apps.append(name)
    else: 
        unique_apps.append(name)

# print('Number of duplicate apps: ', len(duplicates_apps))
# print('\n')
# print(f'Examples of duplicate apps: ', duplicates_apps[:15])

apps_name = ['Instagram', 'Facebook']

# print('\n')
# print('Instagram' in apps_name)
# print('Twitter' in apps_name)

reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])

    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews 

    elif name not in reviews_max:
        reviews_max[name] = n_reviews
# android_clean = {}
# already_added = {}

# for name in reviews_max:
#     if name not in android_clean:
#         android_clean.append(name)

android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name) # make sure this is inside the if block

"""
"""
print(ord('A'))
print(ord('a'))
print(ord('元'))
print(ord('+'))

string = 'abc'

for character in string:
    print(character)
"""


def is_english(string):

    for character in string:
        if ord(character) > 127:
            return False
        else: 
            return True

# print(is_english('Instagram'))
# print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))

print(ord('™'))
print(ord('😜'))