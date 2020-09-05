import csv
import numpy as np

opened_file = open('nyc_taxis.csv')
taxi_list = list(csv.reader(opened_file))
taxi_list = taxi_list[1:]

print(taxi_list)