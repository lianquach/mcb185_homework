import sys 
import mcb185
import itertools 

k = int(sys.argv[2])

kcount = {} # empty dictionary for kmers & their counts 
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1): # typical windowing algorithm
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
	for kmer, n in kcount.items(): print(kmer, n)
	
# generates all possible k-mers and checks them against kcount dictionary 
for nts in itertools.product('ACGT', repeat = k):
	kmer = ''.join(nts) # joins tuple into a string to index our dictionary
	if kmer in kcount: print(kmer, kcount[kmer])
	else:			   print(kmer, 0)
	

