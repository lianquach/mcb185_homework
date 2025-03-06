'''
Prior to doing sequence searches, people often mask low complexity sequence to
prevent finding huge numbers of meaningless alignments. Write a python version.

Input: multi-FASTA file of DNA
Output: multi-FASTA file of DNA with low complexity regions masked
Change all low-complexity regions to 'N' in the output
Provide parameters for fasta file, window size, and entropy
'''

import sys
import math
import mcb185

fas = sys.argv[1]
w = int(sys.argv[2]) # window size
ent = float(sys.argv[3]) # entropy threshold 

def entropy(seq):
	hval = 0.0
	total = len(seq)
	a = seq.count('A') / total
	c = seq.count('C') / total
	g = seq.count('G') / total
	t = seq.count('T') / total
	
	for prob in [a, c, g, t]:
		if prob != 0:
			hval -= prob * math.log2(prob)
	return hval 

for defline, seq in mcb185.read_fasta(fas):

	dust = list(seq)
	
	for i in range(len(seq) - w + 1):
		dna = seq[i:i+w]
		hval = entropy(dna)
		if hval < ent:
			for j in range(i, i + w):
				dust[j] = 'N'
		
	print('>', defline, sep='')
	seq = ''.join(dust)
	
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])
	