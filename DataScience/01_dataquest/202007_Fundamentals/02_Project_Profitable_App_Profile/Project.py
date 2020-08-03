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
print(android[10472])  # Incorrect row
print('\n')
print(android_header)  # header
print('\n')
print(android[0])      # correct row

# remove the incorrect row[10472] using the del statement
print(len(android))
del android[10472]
print(len(android))
"""
