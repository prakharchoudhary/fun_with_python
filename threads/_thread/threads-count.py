import _thread as thread, time

"""
thread basics: start 5 copies of a function running in parallel;
uses time.sleep so that the main thread doesn't die too early--
this kills all other threads on some platforms; stdout is shared:
thread outputs may be intermixed in this version arbitarily.
"""

def counter(myId, count):
	for i in range(count):
		time.sleep(1)
		print('[%s] => %s' % (myId, i))

for i in range(5):				# spawns 5 threads
	thread.start_new_thread(counter, (i, 5))		# each thread loops 5 times

time.sleep(6)
print('Main thread exiting.')		# don't exit too early