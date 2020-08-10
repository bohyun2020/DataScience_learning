"""
# 1. Introducing Data Cleaning
As data scientists, not all data we encounter is clean; 
we often need to prepare it in a process called data cleaning

If we want to find out how many rows are in our list of lists, 
we can use the Python built-in function len()

"""
"""
# 2. Reading our MoMA Data Set
"""
"""
children = [
                ["Ruby", "17", "blue"],
                ["Jack", "5", "red"],
                ["Charlotte", "14", "black"],
                ["Matilda", "7", "orange"],
                ["Noah", "12", "purple"],
                ["Songi", "18", "pink & black"],
            ]

num_rows = len(children)
print(num_rows)
"""
"""
# 1) Example
from csv import reader

opened_file = open('children.csv')
read_file = reader(opened_file)
children = list(read_file)

children = children[1:]
"""
"""
# 2) Exercise
from csv import reader

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)

moma = moma[1:]
"""
"""

# 3. Replacing Substrings with the replace Method
    1) Parts of strings are called substrings.
    2) We can use the str.replace() method to find and replace substrings.
    3) str.replace() requires two arguments:
        1] old : The substring we want to find and replace.
        2] new : The substring we want to replace old with.
    4) When we use str.replace(), we substitute the str for the variable name of  # 중요해요 ****
        the string we want to modify.
    5) We need to use = to assign the modified string to a new variable name.

"""
"""

    # 1) Sample
fav_color = "red is my favorite color"
fav_color = fav_color.replace("red", "pink")
print(fav_color)


fav_color = "red is my favorite color"
fav_color = fav_color.replace("r", "R")
print(fav_color)

fav_color = "red is my favorite color"
fav_color = fav_color.replace("red", "Red")
print(fav_color)

"""
"""
    # 2) Exercise

age1 = "I am thirty-one years old"
age2 = age1.replace("one", "three")
print(age2)
"""
"""
# 4. Cleaning the Nationality and Gender Columns

    In order to replace characters across our whole moma data set, 
    we'll need to perform this "replacement" many times. For this, 
    we can use a for loop.

"""
"""
    # 1) Example
nationalities = ['(American)', '(Spanish)', '(French)']

for n in nationalities:
    clean_open = n.replace("(","")
    clean_both = clean_open.replace(")","")
    print(clean_both)
"""
"""
    # 2) Exercise
for row in moma:
    nationality = row[2]
    gender = row[5]

    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    row[2] = nationality

    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    row[5] = gender

    print(nationality)
    print(gender)
 """
"""
 # 5. String Capitalization

 The Gender column in our data set contains four unique values:

"" (an empty string)
"Male"
"Female"
"male"

we can use a Python string method designed specifically 
for handling capitalization: the str.title() method.

"""
"""
# 1) Example
my_string = "The cool thing about this string is that it has a CoMbInAtIoN" \
" of UPPERCASE and lowercase letters!"

my_string_title = my_string.title()
print(my_string_title)
"""
"""
# 2) Exercise
for row in moma:
    gender = row[5]

    # convert the gender to title case.
    gender = gender.title()

    # if there is no gender, set a descriptive vale
    if not gender:
        gender = "Gender Unknown/Other"

    row[5] = gender
"""
"""
for row in moma:
    # fix the capitalization and missing
    # values for the gender column
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender

    # fix the capitalization and missing
    # values for the nationality column
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality
"""
"""
# 6. Errors During Data Cleaning

    The values are four-digit years, wrapped in parentheses and stored as strings. 
    To clean these columns, we need to:

    1) Remove the parentheses from the start and the end of each value.
    2) Convert the values from the string type to an integer type. 
        This will help us perform calculations with them later.

"""
"""
for row in moma[:5]:
    birth_date = row[3]
    death_date = row[4]
    print([birth_date], [death_date])
"""
""" Result 
['(1947)', '(2013)']
['(1916)', '(2007)']
['(1870)', '(1943)']
['(1861)', '(1944)']
['(1857)', '(1927)']
"""
"""
def clean_convert(date):
    date = date.replace("(", "")
    date = date.replace(")", "")
    date = int(date)
    return date 

birth_date = '(1987)'
cleaned_date = clean_convert(birth_date)
print(cleaned_date)
print(type(cleaned_date))

    # Our function successfully removes the parentheses and converts 
    # the value to an integer type. Unfortunately, our function won't work for 
    # every value in our data set. Let's look at the values in the 32nd row:

birth_date_1 = ""
cleaned_date_1 = clean_convert(birth_date_1)

"""
"""
# One way to handle these scenarios is to use an if statement to make sure 
# we aren't encountering an empty string before we convert our value.

def clean_convert(date):

    if date != "":
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

clean_convert("")


for row in moma:
    begin_date = row[3]
    end_date = row[4]

    begin_date = clean_convert(begin_date)
    end_date = clean_convert(end_date)
    row[3] = begin_date
    row[4] = end_date
"""
"""
# 7. Parsing Numbers from Complex Strings, Part One

1912
1929
1913-1923
(1951)
1994
1934
c. 1915
1995
c. 1912
(1988)
2002
1957-1959
c. 1955.
c. 1970's
C. 1990-1999

This column contains data in many different formats:

    1) Some years are in parentheses("(",")").
    2) Some years have c. or C. before them, indicating that the year is approximate.
    3) Some have year ranges, indicated with a dash(-).
    4) Some have 's to indicate a decade.

"""
"""

    # 1 ) Example

strings = ["good!", "morn?ing", "good?!", "morniZZZZng"]                         # 중요 연습!!!
bad_chars = ["!", "?", "Z"]

def strip_characters(string):  # 각각 char, string이 한개가 있다는 개념으로 만듬 
    for char in bad_chars:
        string = string.replace(char,"")

    return string

cleaned_strings = []
for s in strings:            # strings(많은) 을 for loop 통해서 한개 만들고 위에 function 적용
    s = strip_characters(s)
    cleaned_strings.append(s)

print(cleaned_strings)
"""
"""
# 2 ) Exercise
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]


def clean_convert(string):
    for char in bad_chars:
        string = string.replace(char,"")

    return string

stripped_test_data = []
for d in test_data:
    date = clean_convert(d)
    stripped_test_data.append(date)

print(stripped_test_data)
"""
"""
# 8. Parsing Numbers from Complex Strings, Part Two

There are two different scenarios that we need to cater for 
when converting these to integers:

Some are a single year, e.g. 1912.
Some are ranges of years, e.g. 1913-1923.


Here are the ways we'll treat the various cases:

Where there is a single year, we'll keep it.
Where there is a year range, we'll average the two years.
    => we'll average the two years.

"""
"""
three_peat = "1991-1993"
print(three_peat.split("-"))

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']


def process_date(date):                                                         # 중요합니다. 
    if "-" in date:
        split_date = date.split("-")
        date_one = split_date[0]
        date_two = split_date[1]
        date = (int(date_two) + int(date_one)) / 2
        date = round(date)
    else: 
        date = int(date)
    return date

processed_test_data = []
for d in stripped_test_data:
    d = process_date(d)
    processed_test_data.append(d)

print(processed_test_data)

# Once your code works with the test data, you can then iterate over 
# the moma list of lists. In each iteration:

for row in moma:
    data = row[6]

    data = strip_characters(data)
    data = process_date(data)
    row[6] = data
"""

    # Slice characters from a string by position:
last_five_chars = "This is a long string."[:5]
print(last_five_chars)

    # Concatenate strings:
superman = "Clark" + " " + "Kent"
print(superman)


superman1 = "Clark \
Kent"
print(superman1)

superman2 = "Bohyun" + " " + "Park"
print(superman2)