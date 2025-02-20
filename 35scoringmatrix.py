# A scoring system for aligning nucleotide sequences is often described with 2
# values: match and mismatch. Write a program that can print out a 
# match-mismatch scoring matrix. The alphabet, match, and mismatch are all 
# command line parameters.

import sys 

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

print('  ', end=' ')

for c in alphabet:
	print(c, end='  ') 
print()

for nt1 in alphabet:
	print(nt1, end=' ') 	# prints letter starting each row
	for nt2 in alphabet: 	# fills in matrix
		if nt1 == nt2: print(match, end=' ')
		else: print(mismatch, end=' ')
	print()


