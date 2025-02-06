# A classic programming interview question is to write a program that reports
# the first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. 
# This is a tricky problem. You need to initialize and keep track of 2 
# previous values.

# next number is found by adding up the 2 numbers before it

f1 = -1
f2 = 1
for i in range(10):
	f3 = f1 + f2
	print(f3)
	f1 = f2
	f2 = f3