# Write a program that uses a sliding window algorithm to compute GC
# composition and GC-skew along the length of a sequence. 

import sequence 
import gzip 
import sys 
import mcb185

w = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		print(i, sequence.gc_comp(s), sequence.gc_skew(s))
