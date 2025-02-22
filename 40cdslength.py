# Reports the lengths of protein-coding genes in the E. coli genome. The
# program will need to perform the following tasks as it reads each line of
# the file: skip over comment lines, find CDS features (or skip over all 
# non-CDS features), extract the begin and end coordinates, convert the 
# coordinates to integers, and report the length of the CDS (end - begin + 1).

import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg + 1) 