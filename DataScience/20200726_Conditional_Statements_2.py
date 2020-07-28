# 3. The Average Rating of Non-free Apps
"""
In the diagram below, we created a list of lists named app_and_price, and 
we want to extract the names of the free apps in a separate list.
"""
"""
app_and_price = [['Facebook', 0], ['Instagram', 0],
['Plants vs. Zombies', 0.99], ['Minecraft: Pcket Edition',
6.99], ['Temple Run', 0], ['Plague Inc.', 0.99]
              ]

free_apps = []
for app in app_and_price:
    name = app[0]
    price = app[1]
    
    if price == 0:
        free_apps.append(name)

print(free_apps)


price = 2 
print(2 != 0)
print(2 != 2)

if price != 2:
    print('Price is not equal to 2')
"""
# 4. The Average Rating of Gaming Apps
"""
opend_file = open('AppleStore.csv', encoding = 'UTF-8')

from csv import reader
read_file = reader(opend_file)
apps_data = list(read_file)


rating_gaming_apps = []
rating_non_gaming_apps = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11].lower() # 여기서 lower 소문자로 적용 시키고 아래 45 line을 'games'로 설정하면 된다.     

    if genre == 'games':
        rating_gaming_apps.append(rating)
    else:
        rating_non_gaming_apps.append(rating)

avg_rating_gaming_apps = sum(rating_gaming_apps) / len(rating_gaming_apps)
avg_rating_non_gaming_apps = sum(rating_non_gaming_apps) / len(rating_non_gaming_apps)
print(avg_rating_gaming_apps)
print(avg_rating_non_gaming_apps)
"""
# 5. Multiple Conditions
"""
# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11].lower()
    # Complete code from here
    
    if price == 0.0 and genre == 'games':
        free_games_ratings.append(rating)

avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)
print(avg_rating_free_games)
"""

# 8. Comparison Operators
"""
app_name = 'Ulysses'
app_price = 24.99

if app_price > 20:
    print('This app is expensive!')

print(app_price > 20)
"""
"""
# 1번째 방법 
# apps_4_or_greater = []

opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_4_or_greater = []

for row in apps_data[1:]:
    rating = float(row[7])

    if rating >= 4.0:
        apps_4_or_greater.append(rating)

print(len(apps_4_or_greater))

# 2번째 방법
# n_of_apps = 0

opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

n_of_apps = 0
for row in apps_data[1:]:
    rating = float(row[7])

    if rating >= 4.0:
        n_of_apps += 1 

print(n_of_apps)
"""
"""
# Now let's answer the other three questions:
# 
# 1. What is the average rating of the apps that have a price greater than $9?

opened_file = open('AppleStore.csv', encoding='UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])

    if price > 9.0:
        ratings.append(rating)

avg_rating_apps = sum(ratings) / len(ratings)
print(avg_rating_apps)

# 2. How many apps have a price greater than $9? answer: 
print(len(ratings))

# 3. How many apps have a price smaller than or equal to $9?

print(len(apps_data[1:]))
n_apps_more_9 = len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings) 
print(n_apps_less_9)
"""
"""
# 9. The else Clause
apps_data = [['Call of Duty: Zomebies', 5,0], ['Facebook', 0,0],
['Instagram', 0.0], ['Temple Run', 0.0]
            ]

for app in apps_data:
    price = float(app[1])

    if price == 0.0:
        app.append('free')  # app을 업데이트 하고나면, apps_data도 업데이트 된다. 
    else:
        app.append('non-free')

print(apps_data)
print(apps_data[0])
"""


By adding labels to the end of each row, we basically created a new column. 
Name this column "free_or_not" by appending the string 'free_or_not' 
to the first row of the apps_data data set. Make sure this is done outside the for loop.
Print the header row and the first five rows to see some of the changes we made.

opened_file = open('AppleStore.csv', encoding = 'UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')
apps_data[0].append('free_or_not')
print(apps_data[:6])

"""

# 10. The elif Clause
"""
opened_file = open('AppleStore.csv', encoding = 'UTF-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])

    if price == 0.0:
        app.append('free')
    elif price > 0.0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')

apps_data[0].append('price_label') 
print(apps_data[:6]) # 이런식으로 확인해서 price_label이 첫행에 제대로 들어갔는 지 확인한다.
"""

