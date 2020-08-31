"""

7. The Time Class
    we're going to analyze presidential appointment times. 
    To achieve this, we're going to use the datetime.time class.

    datetime.time(hour=0, minute=0, second=0, microsecond=0)

"""
"""

# 1) Sample
import datetime as dt

two_thirty = dt.time(14, 30)
print(two_thirty)

five_sec_after_8am = dt.time(8, 0, 5)
print(five_sec_after_8am)


"""
"""
# 2) Sample
    # using the datetime.datetime.time() method
    #   Why? -> Another way to represent time 

import datetime as dt

bohyun_birth_date = dt.datetime(1987, 2, 26, 13, 36)
bohyun_birth_time = bohyun_birth_date.time()
print(bohyun_birth_time)

jfk_shot_dt = dt.datetime(1963, 11, 22, 12, 30)
jfk_shot_t = jfk_shot_dt.time()
print(jfk_shot_t)

"""
"""

# 3) Sample
    # 비표준형 -> 표준형
    # datetime.strptime()
    #   Why? -> The time class doesn't have a strptime() constructor

import datetime as dt

time_str = "8:00"
time_dt = dt.datetime.strptime(time_str, "%H:%M")
time_t = time_dt.time()
print(time_dt)
print(time_t)

"""
"""

# 4) Sample
    # 1. time.hour / time.second
    # 2. time.strftime()

import datetime as dt

time_t = dt.time(2, 26)
hour = time_t.hour
minute = time_t.minute   

print(time_t)
print(hour)
print(minute)

time_formatted = time_t.strftime("%H-%M")
print(time_formatted)

"""
"""

# 5) Exercise

appt_times = []
for row in potus:
    app_dt = row[2]
    app_t = app_dt.time()
    app_times.append(app_t)

"""
"""

8. Comparing time objects

    A useful feature of time objects is that they support comparisons.
    We can test if one time is greater - or later - than another:

"""
"""

# 1) Sample

import datetime as dt

t1 = dt.time(6, 30)
t2 = dt.time(15, 30)

comparison = t1 > t2
print(comparison)


"""
"""
# 2) Sample
    # Because these comparison operations are supported, 
    # Python built-in functions like min() and max() can also be used:


import datetime as dt 

times = [
            dt.time(2, 30),
            dt.time(8, 30),
            dt.time(12, 30),
        ]

print(min(times))
print(max(times))


"""
"""

# 3) Exercise 

appt_times = []
for row in potus:
    app_dt = row[2]
    app_t = app_dt.time()
    appt_times.append(app_t)

print(min(appt_times))
print(max(appt_times))


"""
"""
    # 9. Calculations with Dates and Times

    - Just like time objects, datetime objects support comparison operators 
    like > and <.
    - Let's experiment with mathematical operators like - and + to see if they work too

"""
"""
# 1) Sample
#   TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'datetime.datetime'

import datetime as dt

dt1 = dt.datetime(2002, 5, 1)
dt2 = dt.datetime(2002, 4, 1)
print(dt1 + dt2)

"""
"""
# 2) Sample
    # When we use the - operator with two date objects, 
    # the result is the time difference between the two datetime objects

import datetime as dt

dt1 = dt.datetime(2002, 5, 1, 12, 30)
dt2 = dt.datetime(2002, 4, 1, 2, 25)
diff = dt1 - dt2

print(diff)
print(type(diff))

"""
"""

# 3) Sample
    1) We observed that we can create an object of the timedelta class using the - operator, 
    2) but we can also instantiate a timedelta class directly.

    datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

    You might notice that the ordering of the parameters doesn't follow the 
    order you might expect, and for this reason it can be clearer to use keyword
    arguments when instantiating objects if we are using anything other than days:

"""
"""
# Use keyword arguments

import datetime as dt

two_days = dt.timedelta(2)
print(two_days)

three_weeks = dt.timedelta(weeks=3)
print(three_weeks)

time_4 = dt.timedelta(hours=4, minutes=30, seconds=30, weeks=1, microseconds=125, milliseconds=80)
print(time_4) 


# two_days = dt.timedelta(2)
# print(two_days)

# three_weeks = dt.timedelta(weeks=3)
# print(three_weeks)

# time_4 = dt.timedelta(hours=4, minutes=30, seconds=30)
# print(time_4)

"""
"""

# 4) Sample
    # We can also use timedelta objects to add or subtract time from datetime objects

import datetime as dt 

d1 = dt.datetime(1987, 2, 26)
d2 = dt.timedelta(weeks=1)
d1_plus_d2 = d1 + d2
print(d1_plus_d2)

"""
"""
# 5) Exercise

import datetime as dt

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)

print(answer_1)
print(answer_2)
print(answer_3)

"""
"""

# 10. Summarizing Appointment Lengths
    # we're going to use what we've learned to analyze the lengths of meetings

"""
"""
# 1) Sample
import datetime as dt 

start_time = dt.datetime(2020, 8, 31, 9, 30)
end_time = dt.datetime(2020, 8 , 31, 10, 30)
meeting_length = end_time - start_time
print(meeting_length)

"""
"""
# 2) Sample
    # 1. Create a frequency table of the meeting times.
    # 2. Calculate the minimum and maximum value for the appointment lengths.

import datetime as dt

length_counts = {
                    dt.timedelta(minutes=15): 21,
                    dt.timedelta(hours=3): 1,
                    dt.timedelta(seconds=30): 10,
                }

print(min(length_counts))
print(max(length_counts))
print(length_counts)

"""
"""

# 3) Exercise

from csv import reader, writer
import datetime as dt

opened_file = open("potus_visitors_2015.csv")
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")                 # 데이터를 if로 sort 하지? 
    row[3] = end_date

appt_lengths = {}
for row in potus:
    start_date = row[2]
    length = end_date - start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1

print(min(appt_lengths))
print(max(appt_lengths))

"""