# Instead of making a list of birthdays, make a list from the calendar. In the
# previous program, you appended birthdays to a list. In this one, all 
# possible days are already in a list, so assigning a birthday is: 
# calendar[birthday] += 1.

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0

for trial in range(trials):
	#make the empty calendar 
	calendar = []
	for i in range(days):
		calendar.append(0)
	
	# add birthdays 
	for i in range(people):
		bday = random.randint(0, days-1)
		if calendar[bday] == 1:
			shared += 1
			break 
		calendar[bday] += 1
	
print(shared / trials)