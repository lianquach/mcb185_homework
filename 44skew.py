# Re-write 43skew.py as 44skew.py using the more efficient algorithm and then 
# calculate GC-skew and GC composition in 1000 nt windows in the E.coli genome.

import sequence
import sys
import mcb185

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[0:w].count('G')
	c = seq[0:w].count('C')
	
	for i in range(len(seq) -w -1):
		s = seq[i:i+w]
		leaving_nt = seq[i]
		new_nt = seq[i+w]
	
		if leaving_nt == 'G':
			g -= 1
		elif leaving_nt == 'C':
			c -= 1
	
		if new_nt == 'G':
			g += 1
		elif new_nt == 'C':
			c += 1
	
		if g + c == 0:
			skew = 0 
		else: 
			skew = (g - c) / (g + c)
	
		print(i, sequence.gc_comp(s), skew)
