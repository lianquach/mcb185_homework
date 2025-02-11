"""
One of the core mechanics of D&D is the "saving throw". When certain events 
happen, you need to roll a d20 to figure out if you succeed or not.
DC = "difficulty class"
DC 5 = roll 5 or higher to succeed 
DC 10 = roll 10 or higher to succeed 
DC 15 = roll 15 or higher to succeed 
Advantage = roll 2 d20s & take the larger value 
Disadvantage = roll 2 d20s & take the smaller value 

Write a program that simulates saving throws against DCs of 5, 10, 15. Make a 
table showing the probability of success normally, with advantage, and with 
disadvantage. 
"""

import random 

trials = 1000000

def advantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 >= roll2: return roll1
	return roll2

def disadvantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 <= roll2: return roll1
	return roll2
	
# normal rolls 
def normal(dc):
	success = 0
	for i in range(trials):
		roll = random.randint(1, 20)
		if roll >= dc: success += 1
	return success / trials

# advantage rolls 
def adv(dc):
	success = 0
	for i in range(trials):
		roll = advantage()
		if roll >= dc: success += 1
	return success / trials

# disadvantage rolls 
def disadv(dc):
	success = 0
	for i in range(trials):
		roll = disadvantage() 
		if roll >= dc: success += 1
	return success/trials

print("DC", "Normal", "Advantage", "Disadvantage", sep='\t')
print('5', normal(5), adv(5), disadv(5), sep ='\t' )
print('10', normal(10), adv(10), disadv(10), sep ='\t' )
print('15', normal(15), adv(15), disadv(15), sep ='\t' )

	
