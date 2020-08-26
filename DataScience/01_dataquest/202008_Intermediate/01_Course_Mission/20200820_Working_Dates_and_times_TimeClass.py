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
print(time_dt)

time_t = time_dt.time()
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
    appt_times.append(app_t)
"""