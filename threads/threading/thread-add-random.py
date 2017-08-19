"""
-> print different results on each run in windows

This happens because threads overlap arbitrarily in time: statements, even the simple
assignment statements like those here, are not guaranteed to run to completion by
themselves (that is, they are not atomic)
"""

import threading, time
count=0

def adder():
	global count
	count = count + 1		# update a shared name in global scope
	time.sleep(0.5)			# threads share object memory and global names
	count = count + 1

threads  = []
for i in range(100):
	thread = threading.Thread(target=adder, args=())
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

print(count)