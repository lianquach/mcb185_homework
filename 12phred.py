# Write functions that convert quality value symbols into error rates and 
# vice-versa. The ord() function returns the ASCII value of a letter. The
# chr() function turns an ASCII value into a letter. 

import math 

def char_to_prob(c):
	ascii_value = ord(c)
	phred_score = ascii_value - 33
	probability = 10**(-phred_score/10)
	return probability
	
def prob_to_char(p):
	phred_score = -10*math.log10(p)
	ascii_value = phred_score + 33
	character = chr(math.floor(ascii_value))
	return character
	

print(char_to_prob('A'))
print(char_to_prob('B'))
print(char_to_prob('E'))
print(prob_to_char(0.001))
print(prob_to_char(0.0006))
print(prob_to_char(0.00008))
