# String Operation
# The process of linking two or more strings together is called concatenation.
"""
print('This ' + 'is '+ 'a ' + 'sentence.')
print('a' * 6) 


print(type('4.4'))
"""

""" Conditional Statements """
# 1. If statements
"""
opened_file = open('AppleStore.csv', encoding = 'UTF-8')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:     # 0.0로 적용하면 좋다. Price가 float이기 때문에    
        free_apps_ratings.append(rating)
    else:
        non_free_apps_ratings.append(rating)

avg_free_apps_rating = sum(free_apps_ratings) / len(free_apps_ratings)
avg_non_free_apps_rating = sum(non_free_apps_ratings) / len(non_free_apps_ratings)
print(avg_free_apps_rating)
print(avg_non_free_apps_rating)


# 2. Boolean
"""
if True:
    print(100)

# When if statement is followed by False, the code inside the body is not executed
if False:
    print(500) 
"""

