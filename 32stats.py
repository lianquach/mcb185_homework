# Write a program that reports descriptive stats for numbers on the command
# line. Your program should report the following values: number of values, 
# minimum & maximum values, mean & standard deviation, and the median value.

import sys
import math 

count = 0
list = []

# Computes number of values 
for argv in sys.argv[1:]:
	count += 1 
	list.append(count)
print('Number of values:', count)

# Computes minimum and maximum values 
def min_max(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
print('Minimum and maximum values:', min_max(list))

# Computes mean
def mean(vals):
	sum = 0
	for val in vals:
		sum += val
	return sum / len(vals)
print("Mean:", mean(list))

# Computes standard deviation 
def sd(vals):
	summation = 0
	for val in vals:
		summation += (val - mean(vals)) ** 2
	return math.sqrt(summation / count)
print("Standard Devation:", sd(list))

# Computes the median 
def median(vals):
	vals.sort() 
	n = len(vals)
	middle = n // 2
	
	if n % 2 == 0:
		med = (vals[middle - 1] + vals[middle]) / 2
	else: 
		med = vals[middle]
	return med 
print("Median:", median(list))
	