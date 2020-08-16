"""
# 1. Reading our MoMA Data Set
    1) get into the fun part: analyzing the data!

    We'll learn how to:

        (1) Calculate how old the artist was when they created their artwork.
        (2) Analyze and interpret the distribution of artist ages.
        (3) Create functions which summarize our data.
        (4) Print summaries in an easy-to-read-way.

    Even though we don't have to clean the data again, 
    we do have to convert these values to numeric types so we can analyze them.
"""
"""
from csv import reader 


opened_file = open('artworks_clean.csv', encoding='ISO-8859-1')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)

ages = []
for row in moma:
    birth_date = row[3]
    date = row[6]

    if type(birth_date) != int:
        age = 0
    else:
        age = date - birth
    ages.append[age]

final_ages = []
for age in ages:
    if age > 20:
        final_age = age 
    else:
        final_age = "Unknown"
    final_ages.append(final_age)




for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

"""
"""
# 2. Calculating Artist Ages

    is the artist's birth year an int? 
        Yes -> The final age is the artists age
        No -> The final age is "Unknown"

"""
"""
from csv import reader 


opened_file = open('artworks_clean.csv', encoding='ISO-8859-1')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

ages = []
for row in moma:
    birth = row[3]
    date = row[6]

    if type(birth) == int:
        age = date - birth  # date는 이미 위에 int로 다 바꾸었고, ""가 하나도 없는 상태이다. 
    else:
        age = 0
    ages.append(age)                                                            # 이거 중요               

final_ages = []
for age in ages:
    if age <= 20:
        final_age = "Unknown"   # age 라고 variable를 지정하지말고, final_age로 명해야 한다. 안그럼 age에 unknown
    else:                       #   으로 잘못 반영될 수 있으므로 명심할 것 
        final_age = age
    final_ages.append(final_age)

print(final_ages)

"""
"""
# 3. Converting Ages to Decades

    In order to use this technique with our ages, we'll need to:
"""
"""
    # 1) Example
         # 1. Convert the integer value to a string.
         # 2. Use slicing to slice all but the last character.

age1 = 112
decade = str(age1)
decade = decade[:-1]
decade = decade + "0s"
print(decade)



age = 125
decade = str(age)
decade = decade[:-1] 
decade = decade + "0s" # The last thing we need to do is add the substring "0s"
print(decade)
"""
"""
from csv import reader 


opened_file = open('artworks_clean.csv', encoding='ISO-8859-1')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

ages = []
for row in moma:
    birth = row[3]
    date = row[6]

    if type(birth) == int:
        age = date - birth  # date는 이미 위에 int로 다 바꾸었고, ""가 하나도 없는 상태이다. 
    else:
        age = 0
    ages.append(age)                                                            # 이거 중요               

final_ages = []
for age in ages:
    if age <= 20:
        final_age = "Unknown"   # age 라고 variable를 지정하지말고, final_age로 명해야 한다. 안그럼 age에 unknown
    else:                       #   으로 잘못 반영될 수 있으므로 명심할 것 
        final_age = age
    final_ages.append(final_age)

decades = []
for age in final_ages:
    if age == "Unknown":
        decade = "Unknown"      # age 라고 variable를 지정하지말고, decade로 명해야 한다.
    else:
        decade = str(age)      
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)

print(decades)
"""
"""
# 4. Summarizing the Decade Data

    # Frequency table lists how many of each item there are in a collection of items.

    # 1. Sample

"""
"""
fruit = ['orange', 'orange', 'orange', 'banana',
         'apple', 'banana', 'orange', 'banana',
         'apple', 'banana']

fruit_freq = {}
for f in fruit:
    if f in fruit_freq:
        fruit_freq[f] += 1 
    else:
        fruit_freq[f] = 1
print(fruit_freq)

"""
"""
from csv import reader 


opened_file = open('artworks_clean.csv', encoding='ISO-8859-1')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

ages = []
for row in moma:
    birth = row[3]
    date = row[6]

    if type(birth) == int:
        age = date - birth  # date는 이미 위에 int로 다 바꾸었고, ""가 하나도 없는 상태이다. 
    else:
        age = 0
    ages.append(age)                                                            # 이거 중요               

final_ages = []
for age in ages:
    if age <= 20:
        final_age = "Unknown"   # age 라고 variable를 지정하지말고, final_age로 명해야 한다. 안그럼 age에 unknown
    else:                       #   으로 잘못 반영될 수 있으므로 명심할 것 
        final_age = age
    final_ages.append(final_age)


decades = []
for age in final_ages:
    if age == "Unknown":
        decade = "Unkown"
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "Os"
    decades.append(decade)

decade_frequency = {}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1
print(decade_frequency)

"""
"""
# 5. Inserting Variables Into Strings

# 1) Sample 
name = "Kylie"
num = 8

output = name + "'s favorite number is " + str(num)
print(output)

# 2) Sample 
    # As you can see, our code is very easy to understand, 
    #   str.format() converts the integer to a string for us.

output = "{}'s favorite number is {}".format('Bohyun', 7)
print(output)


# 3) Sample
    # If we want to specify ordering and/or repeat numbers, we can use integers:

result_1 = "{0}'s favorite number is {1}. {0}'s favorite number is {1}".format('Bohyun', 7)
print(result_1)

# 4) Sample

    # Keyword arguments
When we use keyword arguments to pass values to str.format(), 
we can use those names inside our braces. Because our string is becoming long, 
we're going to create a separate template string, and call the str.format() 
directly on it:

We recommend being mindful of readability.

If what you're doing has some complexity, using numbers or names 
inside the braces definitely makes things easier!

result_2 ="{name}'s favorite color is {color} \
{color} is {name}'s favorite color.".format(name='Bohyun', color='Blue')
print(result_2)

"""
"""
    # Exercise
artist = "Pablo Picasso"
birth_year = 1881

output1 = "{}'s birth year is {}".format(artist, birth_year)
output2 = "{0}'s birth year is {1}".format(artist, birth_year)
output3 = "{artist}'s birth year is {birth_year}".format(artist="Pablo Picasso", birth_year="1881")
print(output1)
print(output2)
print(output3)

    # 답 중요! 꼭 기억하자 
template = "{name}'s birth year is {year}"
output4 = template.format(name=artist, year=birth_year)                         # 중요**********************
print(output4)

"""
"""

    # 6. Creating an Artist Frequency Table

from csv import reader 


opened_file = open('artworks_clean.csv', encoding='ISO-8859-1')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

ages = []
for row in moma:
    birth = row[3]
    date = row[6]

    if type(birth) == int:
        age = date - birth  # date는 이미 위에 int로 다 바꾸었고, ""가 하나도 없는 상태이다. 
    else:
        age = 0
    ages.append(age)                                                            # 이거 중요               

final_ages = []
for age in ages:
    if age <= 20:
        final_age = "Unknown"   # age 라고 variable를 지정하지말고, final_age로 명해야 한다. 안그럼 age에 unknown
    else:                       #   으로 잘못 반영될 수 있으므로 명심할 것 
        final_age = age
    final_ages.append(final_age)


decades = []
for age in final_ages:
    if age == "Unknown":
        decade = "Unkown"
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "Os"
    decades.append(decade)

decade_frequency = {}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1 

# 1) Sample
gender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1 

artist_freq = {}                                                                                
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1 
print(artist_freq)


"""
