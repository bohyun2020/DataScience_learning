pened_file = open('AppleStore.csv', mode='r', encoding='UTF8')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]        # 이 방법 익히기 1
apps_data = apps_data[1:]    # 이 방법 익히기 2

rating_sum = 0
for row in apps_data:
    rating = float(row[8])   # Float을 적용해서 str -> float으로 바꾸기 
    rating_sum += rating
print(rating_sum)

print(apps_data[1][8])
type(apps_data[1][8])