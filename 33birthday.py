# Write a program that simulates the problem by filling up classrooms of
# students with randomly chosen birthdays. Make the number of days in the
# calendar and the number of people in the classroom command line arguments.
# You will have to run this thousands of times to get an accurate estimate, so
# have a parameter for the number of trials.

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0

for trial in range(trials):
	birthday = []
	for i in range(people):
		bday = random.randint(0, 364)
		if bday in birthday: 
			shared += 1
			break 
		else: 
			birthday.append(bday)

print(shared/trials)