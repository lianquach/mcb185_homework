import argparse
import mcb185 
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
# -- changes them to named parameters & can appear in any order
parser.add_argument('-s', '--size', type=int, default=20, 
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
parser.add_argument('--wrap', type=int, default=60)
arg = parser.parse_args() # harvests values on CL & assigns them

# prints if given proper number and type of arguments 
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

def entropy(seq):
	hval = 0.0
	a = seq.count('A') / len(seq)
	c = seq.count('C') / len(seq)
	g = seq.count('G') / len(seq)
	t = seq.count('T') / len(seq)
	
	for prob in [a, c, g, t]:
		if prob != 0.0:
			hval -= prob * math.log2(prob)
	return hval 

for defline, seq in mcb185.read_fasta(arg.file):
	mask = list(seq)
	for i in range(len(seq) - arg.size + 1):
		win = seq[i:i+arg.size]
		if entropy(win) < arg.entropy:
			for j in range(i, i + arg.size):
				if arg.lower: 
					mask[j] = seq[j].lower()
				else: mask[j] = 'N'
	print('>', defline)		
	mask = ''.join(mask)
	for i in range(0, len(seq), arg.wrap):
		print(mask[i:i+arg.wrap])