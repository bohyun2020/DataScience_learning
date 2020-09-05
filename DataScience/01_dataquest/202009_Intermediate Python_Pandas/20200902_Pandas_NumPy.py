"""

1. NumPy and pandas.
    Luckily, there are two NumPython libraries that allow us to write code quickly 
    without sacrificing performance

2. The core data structure in NumPy is the ndarray or n-dimensional array
    1) In programming, array describes a collection of elements, similar to a list.
    2) The word n-dimensional refers to the fact that ndarrays can have one 
    or more dimensions.


"""
"""

2. Introduction to Ndarrays

    we can directly convert a list to an ndarray using the numpy.array() constructor

"""
"""

# 1) Sample
import numpy as np

data_ndarray = np.array([5, 10, 15, 20])
print(data_ndarray)


# 2) Exercise

import numpy as np

data_ndarray = np.array([10, 20, 30])
print(data_ndarray)

"""
"""

3. Understanding Vectorization

- ndarrays and the NumPy library make it easier to manipulate and analyze data.

1) we used lists of lists to represent data sets.
   they aren't very good for working with larger data set

2) Python - bytecode
   Numpy library - SIMD(Single Instruction Multiple Data) -  

    -> As a result, the NumPy version of our code would only take two processor 
       cycles a four times speed-up!

   This concept of replacing for loops with operations applied to multiple 
   data points at once is called vectorization and ndarrays make vectorization possible.

"""
"""
# 1) Sample

my_numbers = [
				[6, 5],
				[1, 3],
				[4, 6],
			 ]

sums = []

for row in my_numbers:
	row_sum = row[0] + row[1]
	sums.append(row_sum)

print(sums)

"""
"""

4. NYC Taxi-Airport Data

    : two-dimensional (2D) ndarrays

"""
"""
# 1) Sample

import numpy as np

# our list of lists is stored as data_list
data_ndarray = np.array(data_list)


"""
"""
# 2) Exercise

import csv
import numpy as np 

opened_file = open('nyc_taxis.csv')
taxi_list = list(csv.reader(opened_file))
taxi_list = taxi_list[1:]

# Convert all values to floats.

converted_taxi_list = []
for row in taxi_list:
	converted_row = []
	for item in row:
		item = float(item)
		converted_row.append(item)
	converted_taxi_list.append(converted_row)

# Start writing your code below this comment
taxi = np.array(converted_taxi_list)	
print(taxi)

"""
"""

5. Array Shapes

"""
"""
# 1) Sample

import numpy as np

data_ndarray = np.array([[5, 10, 15],
                         [20, 25, 30]])
print(data_ndarray.shape)


"""
"""
# 2) Exercise   

import csv
import numpy as np 

opened_file = open('nyc_taxis.csv')
taxi_list = list(csv.reader(opened_file))
taxi_list = taxi_list[1:]


# Convert all values to floats.
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

taxi_shape = taxi.shape
print(taxi_shape)

"""
"""

6. Selecting and Slicing Rows and Items from ndarrays

	1) Next, let's look at a comparison between working with ndarrays and 
	list of lists to select one or more rows of data:

"""
"""
(1) Sample

# 1) Selecting a single row
	: Same syntax as list of lists. Produce a 1D ndarray.
sel_lol = data_lol[1]
sel_np = data_np[1]

# 2) Selecting multiple rows 
	: Same syntax as list of lists. Produce a 2D ndarray.
sel_lol = data_lol[2:]
sel_np = data_np[2:]

# 3) Selecting a single item.
	# Comma separated row/column locations. Produces a single Python Object.
sel_lol = data_lol[1][3]
sel_np = data_np[1, 3]

"""
"""
# 1) Exercise

import csv
import numpy as np 

opened_file = open('nyc_taxis.csv')
taxi_list = list(csv.reader(opened_file))
taxi_list = taxi_list[1:]


# Convert all values to floats.
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

row_0 = taxi[0]					# a list of lists = same
row_0 = taxi[0]
print(row_0)

row_391_to_500 = taxi[391:501]	# a list of lists = same
print(row_391_to_500)

row_21_column_5 = taxi[21,5]   # a list of lists = taxi[21][5]
print(row_21_column_5)

"""
"""

7. Selecting Columns and Custom Slicing ndarrays

	ndarray[row_index,column_index]

"""
"""

- 헷갈리지 말기

# sel_np = data_np[:,3]

# 참고) String format이랑 비슷해서 헷갈리지 않게 예시 
# name = 'bohyun'
# age = 33.6

# formatted_string = "{} is {:.2f} years old".format(name, age)
# print(formatted_string)

"""
"""
# 1) Select a single column 
	# Produce a 1D ndarray

sel_lol = []
for row in data_lol:
	col4 = row[3]
	sel_lol.append(col4)

sel_np = data_np[:,3]

# 2) Selecting multiple columns
	# Produce a 2D ndarray

sel_lol = []
for row in data_lol:
	col_23 = row[1:3]
	sel_lol.append(col_23)

sel_np = data_np[:,1:3]

# 3) Selecting multiple Columns                                                        # 중요합니다.                                                                                                    
	# Produces a 2D ndarray

sel_lol = []
for row in data_lol:
	cols = [row[1], row[3], row[4]]
	sel_lol.append(cols)

cols = [1, 3, 4]
sel_np = data_np[:,cols]

# 4) Selecting a 1D slice (row)

sel_lol = data_lol[2][1:4]
sel_np = data_np[2, 1:4]

# 5) Selecting a 1D slice (column)

sel_lol = []
rows = data_lol[1:]
for r in rows:
	col5 = row[4]
	sel_lol.append(col5)

sel_np = data_np[1:, 4]

# 6) Selecting a 2D slice

sel_lol = []
rows = data_lol[1:4]
for row in rows:
	sel_lol.append(row[:3])

sel_np = data_np[1:4, :3]

"""

import csv
import numpy as np 

opened_file = open('nyc_taxis.csv')
taxi_list = list(csv.reader(opened_file))
taxi_list = taxi_list[1:]


# Convert all values to floats.
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

# 7) Exercise
columns_1_4_7 = taxi[:,[1, 4, 7]]
row_99_columns_5_to_8 = taxi[99, 5:9]
rows_100_to_200_column_14 = taxi[100:201,14]