"""
thread class instance with state and run() for thread's actions;
uses higher level java-like threading module object join method(not
mutexes or shared global vars) to know when threads are done in main
parent thread.
"""

import threading

class Mythread(threading.Thread):		# subclass THread object
	def __init__(self, myId, count, mutex):
		self.myId = myId
		self.count = count				#per-thread state information
		self.mutex = mutex 				# shared objects, not globals
		threading.Thread.__init__(self)

	def run(self):						# run provides thread logic
		for i in range(self.count):		# still sync stdout access
			with self.mutex:
				print('[%s => %s]' % (self.myId, i))

stdoutmutex = threading.Lock()			# same as thread.allocate_lock()
threads = []
for i in range(10):
	thread = Mythread(i, 100, stdoutmutex)	# make/start 10 threads
	thread.start()							# starts run method in a thread
	threads.append(thread)

for thread in threads:
	thread.join()
print('Main thread exiting.')				# wait for thread exits.

# IMPORTANT:
"""
The Thread.join method used near the end of this script, for instance, waits until 
the thread exits (by default); we can use this method to prevent the main thread from 
exiting before its children, rather than using the time.sleep calls and global locks 
and variables we relied on in earlier threading examples.
"""
