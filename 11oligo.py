# Write a function that returns the oligo melting temperature given the
# number of As, Cs, Gs, and Ts in the oligo Use these two methods. 
# 1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
# 2. For longer oligos, Tm = 64.9 + 41*(G+C-16.4)/(A+T+G+C)

def tm(A, C, G, T):
	if A + C + G + T <= 13:
		return (A+T)*2 + (G+C)*4
	else:
		return 64.9 + 41*(G+C-16.4)/(A+T+G+C)

print(tm(5, 7, 3, 4))
print(tm(10, 20, 30, 40))
print(tm(1, 2, 3, 4))
print(tm(2, 2, 2, 2))