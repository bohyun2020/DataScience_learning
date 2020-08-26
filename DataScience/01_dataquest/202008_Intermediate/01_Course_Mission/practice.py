import datetime as dt

date_1_str = "24/12/1984"
date_1_dt = dt.datetime.strptime(date_1_str, "%d/%m/%Y")
print(type(date_1_dt))
print(date_1_dt)