# Write a program that provides the closest official color name given some
# red, green, and blue values. For example, given the color values 200, 0, 50,
# your program should report a shade of red.

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
	
def closest_color(colorfile, R, G, B):
	mini = 765
	closest = ''

	with open(colorfile) as fp:
		for line in fp:
			words = line.split()
			name = words[0]
			hexcode = words[1]
			r, g, b = words[2].split(',')
			rgb = (int(r), int(g), int(b))

			dist = dtc([R, G, B], rgb)
			if dist < mini:
				mini = dist 
				closest = name
	return closest

print(closest_color(colorfile, R, G, B))
