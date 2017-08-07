"""
use mutex locks to know when threads are done in main/parent thread,
instead of time.sleep. lock stdout to avoid comingled prints;
"""

import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myId, count):
	for i in range(count):
		stdoutmutex.acquire()
		print('[%s] => %s'%(myId, i))		 
		stdoutmutex.release()
	exitmutexes[myId].acquire()		#single main thread

for i in range(10):
	thread.start_new_thread(counter, (i,100))

for mutex in exitmutexes:
	while not mutex.locked(): pass
print('Main thread exiting.')