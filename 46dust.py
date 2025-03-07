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

w = int(sys.argv[2]) # window size
ent = float(sys.argv[3]) # entropy threshold 

def entropy(sequence):
	hval = 0.0
	a = sequence.count('A') / len(seq)
	c = sequence.count('C') / len(seq)
	g = sequence.count('G') / len(seq)
	t = sequence.count('T') / len(seq)
	
	for prob in [a, c, g, t]:
		if prob != 0:
			hval -= prob * math.log2(prob)
	return hval 

for defline, seq in mcb185.read_fasta(sys.argv[1]):

	mask = list(seq) # converts nucs into list
	
	for i in range(len(seq) - w + 1):
		win = seq[i:i+w]
		if entropy(win) < ent:
			for j in range(i, i + w):
				mask[j] = 'N'
		
	print('>', defline, sep='')
	mask = ''.join(mask)
	
	for i in range(0, len(seq), 60):
		print(mask[i:i+60])
