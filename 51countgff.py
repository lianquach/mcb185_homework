import gzip 
import sys 

count = {} # creates empty dictionary, key = feature, value = # of times seen
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0 # creates a key
		count[feature] += 1 # assumes that feature is already in table
	for f, n in count.items(): print(f, n)
	for k in sorted(count): print(k, count[k]) # alphabetical order