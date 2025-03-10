# set = mutable container, but all elements are unique & not ordered 
# set has {}, efficient for looking things up 
s = {'A', 'C', 'G'}
print(s)

# add items to a set with add() method 
s.add('T')
print(s)
s.add('A')
print(s) # adding the same element doesn't do anything 

import random
import time

# dictionary = like a list, but indices are strings instead of #'s
# each item exists as a key:value pair 
# key is string in [], variable is anything you can put in a variable
# dictionary = key:value pairs, sets are just values 

# create a empty dictionary 
d = {}
d = dict()
d = {'dog': 'woof', 'cat': 'meow'}
print(d)

# access items with []
print(d['cat'])

# add item to dictionary, assign new key:value pair 
d['pig'] = 'oink' 
print(d)

# change value of an item, access it with its key 
d['cat'] = 'mew' 
print(d)

# use del to delete an item 
del d['cat']
print(d)

# check if a key exists, use keyword 'in'
if 'dog' in d: print(d['dog'])

# ways to iterate through a dictionary 
for key in d: print(f'{key} says {d[key]}')
# .items() = displays list of dictionary key-value pairs 
for k,v in d.items(): print(k, 'say', v) # most common way 
print(d.keys(), d.values(), list(d.values()))

'''
# Nucleotide composition, but with dictionaries 
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1

# sort by keys 
for k in sorted(count): print(k, count[k])
'''

# use itertools.product() to generate all possible kmers 
import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)
    
# usage statement = brief synopsis of how to use the command
# should state what the command does & what options + arguments it takes 

# named arguments are optional & can occur in any order 
print('first', 'second')                       # positional only
print('first', 'second', sep='\t', end='\n')   # named
print('first', 'second', end='\n', sep='\t')   # named, different order