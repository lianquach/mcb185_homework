# Unit 2 Assessment 
# 51...1 by 2's 
# if prime follow with *

def is_prime(n):
	for den in range(2, n //2 + 1):
		if n % den == 0: return False
	return True 
	
for i in range(51, 0, -2):
	if is_prime(i) == True: 
		print(i, "*")
	else: 
		print(i)