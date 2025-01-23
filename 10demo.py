# 10demo.py by Lian Quach

import math
print ('hello, again') # greeting
print(1.5e-2)
print(11 % 3)
print (8 * (8 + 3))
print (math.sqrt(81))
print(math.e)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='\n')

def hypotenuse(a, b):
	c = (a**2 + b**2)**0.5
	return c
x = hypotenuse(3,4)
print(x)
