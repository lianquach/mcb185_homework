import sys 
import mcb185 

# works for both normal & compressed files 
# each iteration of for loop retrieves the next record from the FASTA file
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	# each record is returned aas a tuple 
	print(defline[:30], seq[:40], len(seq))