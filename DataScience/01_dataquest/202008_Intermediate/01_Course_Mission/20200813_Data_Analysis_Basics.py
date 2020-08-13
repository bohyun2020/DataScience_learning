"""
# 7. Creating an Artist Summary Function

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

# 1) Sample
gender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1
print(gender_freq)

# 2) Exercise
artist_freq = {}                                                                                
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1 



def artist_summary(artist):
    num_artworks = artist_freq[artist]
    template = "There are {num} artworks by {name} in the data set"
    output = template.format(name=artist, num=num_artworks)
    print(output)

artist_summary("Henri Matisse")
"""
"""
# 8. Formatting Numbers Inside Strings                                          * 매우 중요

 One other powerful usage of the method is its ability to help us apply 
 formatting to numbers as they are inserted into the string. 
 This can make our data more readable, especially in the case of long decimal numbers
"""
"""
    # 1) Sample
        For most cases, having six numbers after the decimal point 
        — also called precision — is unnecessary.
"""
"""
num = 32.554865
print("I own {pct}% of the company".format(pct=num))

"""
"""
    2) Sample
    We specify number formatting, including things like precision, 
    by adding one of various format specifications inside the braces ({}) of our string.
"""
"""
print("I own {pct:.2f}% of the company".format(pct=32.554865))
print("I own {:.2f}% of the company".format(32.554865))

"""
"""

    3) Sample
    : Another useful format specification is to add a comma as a thousands 
    separator, which prevents large numbers from being hard to read,
    like in the example below:

    Tip) The easy way to remember this order is that in a number like 3,412.69, #### 레알 꿀팁 #####
    the comma comes before the decimal point in the same way the thousands 
    separator comes before the precision.

"""
"""
print("The approximate population of {0} is {1}".format("India",1324000000))
print("The approximate population of {0} is {1:,}".format("India",1324000000))

print("Your bank balance is ${bal:,.2f}".format(bal=12345.678))
"""
"""
    #4 ) Exercise

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

# 1) 내가 푼 것 

for row in pop_millions:
    country = row[0]
    n_population = row[1]
    template = "The population of {name} is {population:,.2f} million"
    output = template.format(name=country, population=n_population)
    print(output)

# 2) 해설 
template = "The population of {} is {:,.2f} million"

for country in pop_millions:
    name = country[0]
    pop = country[1]
    output = template.format(name, pop)
    print(output)
"""

# 9. Challenge: Summarizing Artwork Gender Data

"""
    # 1) Sample

fruit_freq = {
    'orange': 4,
    'banana': 4,
    'apple': 2
}

for fruit, qty in fruit_freq.items():
    output = "I have {q} {f}s".format(f=fruit, q=qty)
    print(output)
"""
"""
    # 2) Exercise
from csv import reader 


opened_file = open('artworks_clean.csv', encoding='ISO-8859-1')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

gender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1

template = "There are {f:,.2f} artworks by {g} artists"
for gender, freq in gender_freq.items():
    output = template.format(g=gender, f=freq)
    print(output)

"""