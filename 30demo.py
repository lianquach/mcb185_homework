# use double quotes inside single quotes or single quotes inside double quotes
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

# use \ to tell python you aren't using it as a delimiter
print('hey "dude" don\'t tell me what to do')

s = 'helloworld'
print(s.upper())
print(s)

print(s.replace('o', '')) # removes any o letter
print(s.replace('o', '').replace('r', 'i')) # removes o + replaces r with i

import math 

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

# iterate through characters in a string 
for nt in seq:
    print(nt, end='')
print() 

# iterate through letters by indices 
for i in range(len(seq)):
	print(i, seq[i])

# slice = subset of a container 
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2]) # step size of 2 
print(s[0:5], s[:5])        # omit initial value 
print(s[5:len(s)], s[5:])   # omit final value, which is length of string 
print(s, s[::], s[::1], s[::-1])

# splice a string into codons 
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)

# tuples are immutable like strings, can also be indexed + sliced 
tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax)                       # note the parentheses in the output
print(tax[0])      # index
print(tax[::-1])   # slice

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

# enumerate(), provides a tuple containing the index + value 
for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

# zip(), retrieves an element from each container & returns them in a tuple 
for nt, name in zip(nts, names):
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

# lists 
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

# add elements to end of list
nts.append('C')
print(nts)

# remove elements from end of list 
last = nts.pop()
print(last)

# sort a list, cannot mix strings
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

# make a new variable to an existing list ==> creates another name of the list 
# modifications happen to both nucleotides & nts 
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list() function w/out arguments creates empty lists
items = list()
print(items)
items.append('eggs')
print(items)

# or create empty lists w/ []
stuff = []
stuff.append(3)
print(stuff)

# convert a string into a list of letters 
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# split strings into lists of strings 
text = 'good day          to you'
words = text.split()
print(words)

# turn lists into strings by joining them w/a delimiter
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

import sys
print(sys.argv) # printed name of program 

i = int('42')
x = float('0.61803')
print(i * x)