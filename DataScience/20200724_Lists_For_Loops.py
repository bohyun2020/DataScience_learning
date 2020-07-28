#opened_file = open('01_dataquest/appleStore.csv', encoding='UTF8') # The output is an object
# AppleStore.csv file will open once open('AppleStore.csv') has finished running.

#from csv import reader
#read_file = reader(opened_file)
#apps_data = list(read_file)

#print(len(apps_data))
#print(apps_data[0])
#print(apps_data[1:3])
# Now that we've read the file, we can transform it into a list of lists using the list()
# The apps_data variable above is a list of lists, and it stores a data set of 7,197 rows and 16 columns.


# 08 Repetitive Process 
"""
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum = 0
for each_list in app_data_set:
    rating = each_list[-1]
    rating_sum += rating
avg_rating = rating_sum / len(app_data_set)  # len(app_data_set)로 생각해야함.
print(avg_rating)

"""
# 10. Average App rating
"""
"""
"""
opened_file = open('AppleStore.csv', mode='r', encoding='UTF8')


from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]        # 이 방법 익히기 1
apps_data = apps_data[1:]    # 이 방법 익히기 2

rating_sum = 0
for row in apps_data:
    rating = float(row[8])   # Float을 적용해서 str -> float으로 바꾸기  
    rating_sum += rating     # 왜냐하면, '4.5' 처럼 str으로 표현될 수 있기 때문에

avg_rating = rating_sum / len(apps_data)
print(avg_rating)

"""
# 11. Alternative Ways to Compute an Average.
"""
a_list = [1, 2]
a_list.append(3)
print(a_list)

empty_list = []
empty_list.append('12')  # ''이 없으면 int로 들어가고, ''있으면 str으로 반영
print(empty_list)
print(type(empty_list[0]))


opened_file = open('AppleStore.csv', mode='r', encoding='utf-8')


from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
for row in apps_data[1:]:
    rating = float(row[7])   # Float을 적용해서 str -> float으로 바꾸기 
    ratings.append(rating)   # Append method 사용해서 Rating List에 추가하기 

avg_rating = sum(ratings) / len(ratings)
print(avg_rating)

# A data point is a value that offers us some information.
# A set of data points make up a data set. A table is an example of a data set.
# Lists are data types which we can use to store data sets.
# Repetitive process can be automated using for loops.
"""