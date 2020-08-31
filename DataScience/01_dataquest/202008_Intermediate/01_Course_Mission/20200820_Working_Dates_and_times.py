"""
from csv import reader, writer

opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]
"""
"""
# 3. The Datetime Module

    # 1) Import the whole module by name 

import datetime

my_datetime_object = datetime.datetime()



    # 2) Import definitions via name or wildcard

from datetime import datetime
from datetime import *

my_datetime_object = datetime()

    # 3) Import whole module by alias

import datetime as dt

my_datetime_object = dt.datetime()

"""
"""

# 4. The Datetime Class
    - datetime.datetime(year, month, day, hour=0, minute=0, second=0)

"""
"""

# 1) Sample
import datetime as dt

god_birth = dt.datetime(1987, 2, 26, 13, 36)
print(god_birth)

god_birth_2 = dt.datetime(1987, 2, 26)
print(god_birth_2)

god_birth_3 = dt.datetime(1955, 12, 15)
print(god_birth_3)

"""
"""
    # 2) Exercise   

import datetime as dt 

ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17, 30)
print(man_on_moon)


"""
"""
# 5. Using Strptime to Parse Strings as Dates

The datetime.strptime() constructor returns a datime object defined using a
special syntax system to describe date and time formats called strftime.

The strftime syntax uses a series of format codes consisting of a % character
which specifies a date or time part in a particular format. 


"""
"""
# 1) Sample
import datetime as dt


date_string = '12/18/15 16:30'

date, time = date_string.split()
month, day, year = date.split("/")
hour, minute = time.split(":")

month = int(month)
day = int(day)
year = int(year)
hour = int(hour)
minute = int(minute)


dt_object = dt.datetime(year, month, day, hour, minute)
print(dt_object)


"""
"""
# 2) Sample
    # 비표준형 포맷을 표준형으로 바꾸는 경우
    # strptime(string, strftime syntax) constructor 사용

import datetime as dt

date_1_str = "26/02/1987"
date_format = "%d/%m/%Y"
date_1_obj = dt.datetime.strptime(date_1_str, date_format)
print(date_1_obj)

"""
"""
# 3) Exercise                                                                   # 모르겠음 - if를 써서 이상한 것만 수정해야함

from csv import reader, writer
import datetime as dt

opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

data_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date, data_format)
    row[2] = start_date


"""
"""
# 6. Using Strftime to format dates

The datetime class has a number of attributes

    datetime.day: The day of the month.
    datetime.month: The month of the year.
    datetime.year: The year.
    datetime.hour: The hour of the day.
    datetime.minute: The minute of the hour.

"""
"""
    # 1) Sample

import datetime as dt

dt_object = dt.datetime(1987, 02, 26)

day = dt_object.day
month = dt_object.month
year = dt_object.year

dt_string = "{}/{}/{}".format(year, month, day)
print(dt_string)

"""
"""

     the datetime class has a datetime.strftime() method which will return 
     a string representation of the date using the strftime syntax

    (1) strptime >> str-p-time >> string parse time
    (2) strftime >> str-f-time >> string format time


"""
"""
# 2) Sample 

import datetime as dt

dt_object = dt.datetime(1987, 2, 26, 13, 36)

dt_object = dt.datetime(1987, 2, 26, 13, 36)
dt_string = dt_object.strftime("%m-%d-%Y --%H:%M--")
print(dt_string)

"""
"""
# 3) Exercise

from csv import reader, writer
import datetime as dt

opend_file = open("potus_visitors_2015.csv")
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date, date_format)
    row[2] = start_date

visitors_per_month = {}

for row in potus:
    month_dt = row[2]
    month_str = month_dt.strftime("%m-%d-%Y")                                   # dt.datetiime이 왜 안왔는지 이해
    if month_str not in visitors_per_month:
        visitors_per_month[month_str] = 1
    else:
        visitors_per_month[month_str] += 1
"""
