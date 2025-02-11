"""
Death saves are a little different than normal saving throws. If your health
drops to 0 or below, you are unconscious and may die.
1 = 2 failures 
2 - 9 = failure
10 - 19 = success
20 = revived 
3 failures = death
3 successes = stable

Write a program that simulates death saves. What is the probability one dies, 
stabilizes, or revives? 
"""
import random

trials = 1000000
death = 0
stable = 0
revive = 0

for i in range(trials):
	success = 0
	failure = 0
	
	while True: 
		roll = random.randint(1,20)
		if roll == 1: 
			failure += 2
			if failure >= 3:
				death += 1
				break 
		elif roll < 10: 
			failure += 1
			if failure >= 3:
				death += 1
				break
		elif roll < 20: 
			success += 1
			if success >= 3:
				stable += 1
				break
		else: 
			revive +=1
			break

print("Probability of death:", death / trials)
print("Probability of revival:", revive / trials)
print("Probaility of stabilization:", stable / trials)
			
		