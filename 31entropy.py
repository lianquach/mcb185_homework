import sys
import math 

probs = []
# harvest words on command line & turns them into probabilities 
for arg in sys.argv[1:]:
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: not a probability')
	probs.append(f)

# check if the sum of the probs on command line are equal to 1.0
total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
	sys.exit('error: probs must sum to 1.0')

# calculate Shannon entropy 
h = 0
for p in probs: 
	h -= p * math.log2(p)

print(f'{h:.4f}')