''' 
Write a program that finds the open reading frames in the E. coli genome.

Input: multi-FASTA file of DNA
Output: multi-FASTA file of proteins
Must perform a six-frame translation
Proteins must be at least 100 amino acids long
Proteins must start with 'M' and end with '*'
Deflines must have unique identifiers
'''
import sys 
import mcb185 
import sequence 

length = int(sys.argv[2])

def protein_finder(seq, length, label):
	for i in range(3): 
		frame = 0
		protein_seq = mcb185.translate(seq[i:])
		ps = list(protein_seq)
		
		# mark end of protein that doesn't end in stop codon
		if ps[len(ps) - 1] != '*': ps.append('-')
		ps_str = ''.join(ps)
		
		orfs = ps_str.split('*')
		for orf in orfs:
			if 'M' not in orf: continue 
			idx = orf.index('M')
			protein = orf[idx:]
			if len(protein) >= length and '-' not in protein:
				print('>', name, '-prot-', label, '-', frame, sep='')
				print(protein, '*', sep='')
				frame += 1

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	revseq = sequence.revcomp(seq)
	protein_finder(seq, length, 'for')
	protein_finder(revseq, length, 'rev')