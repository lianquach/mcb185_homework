'''
Write a program that predicts which proteins in a proteome are transmembrane.
Transmembrane proteins are characterized by having:

- a hydrophobic signal peptide near the N-terminus
- other hydrophobic regions to cross the plasma membrane

Hydrophobicity can be measured in many ways. We'll use Kyte-Doolittle for its
historical importance.

- signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
- transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa
'''

import sequence
import sys
import mcb185	

def hydrophobicity(seq, l, average):
	for i in range(0, len(seq) - l + 1):
		s = seq[i:i+l]
		score = 0
		
		# proline not contained in signal peptide or TM region
		if 'P' in s: continue
		
		for aa in s:
			if 	 aa == 'I': score += 4.5
			elif aa == 'V': score += 4.2
			elif aa == 'L': score += 3.8
			elif aa == 'F': score += 2.8
			elif aa == 'C': score += 2.5
			elif aa == 'M': score += 1.9
			elif aa == 'A': score += 1.8
			elif aa == 'G': score += -0.4
			elif aa == 'T': score += -0.7
			elif aa == 'S': score += -0.8
			elif aa == 'W': score += -0.9
			elif aa == 'Y': score += -1.3
			elif aa == 'P': score += -1.6
			elif aa == 'H': score += -3.2
			elif aa == 'E': score += -3.5
			elif aa == 'Q': score += -3.5
			elif aa == 'D': score += -3.5
			elif aa == 'N': score += -3.5
			elif aa == 'K': score += -3.9
			elif aa == 'R': score += -4.5
		
		kd = score / l
		if kd >= average: 
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if hydrophobicity(seq[:30], 8, 2.5) and hydrophobicity(seq[30:], 11, 2.0): print(defline)