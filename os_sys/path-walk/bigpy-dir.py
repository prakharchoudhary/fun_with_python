"""
Finds largest file in a single directory
"""

import os, glob, sys
dirname = '/home/pc' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
	filesize = os.path.getsize(filename)
	allsizes.append((filesize, filename))
	# Why did we put the size first?
	# ==> because size appears first in the list’s tuples, it will
	#	dominate the ascending value sort

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])