## 2. Lists of lists ##

import csv
world_alcohol = list(csv.reader(open("world_alcohol.csv")))
years=[]
for row in world_alcohol:
    years.append(row[0])
years = years[1:]
total = 0
for item in years:
    total = total + float(item)
avg_year = total / len(years)
print(avg_year)

## 4. Using NumPy ##

import numpy as np
world_alcohol = np.genfromtxt("world_alcohol.csv", delimiter = ',')
print(type(world_alcohol))

## 5. Creating arrays ##

import numpy
vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

## 6. Array shape ##

vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape

## 7. Data types ##

import numpy
world_alcohol_dtype = world_alcohol.dtype

## 9. Reading in the data properly ##

import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol)

## 10. Indexing arrays ##

import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
for row in world_alcohol:
    if row[2]=="Uruguay" and row[3] == 'Other' and row[0]=='1986':
        uruguay_other_1986=row[4]
third_country = world_alcohol[2][2]

## 11. Slicing arrays ##

countries=world_alcohol[:,2]
alcohol_consumption=world_alcohol[:,4]

## 12. Slicing one dimension ##

first_two_columns = world_alcohol[:,:2]
first_ten_years = world_alcohol[:10,0]
first_ten_rows = world_alcohol[:10,:]

## 13. Slicing arrays ##

first_twenty_regions = world_alcohol[:20,1:3]