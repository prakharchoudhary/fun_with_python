"""
synchronize acces to stdout: because it is shared global,
threads outputs may be intermixed if not synchronnized
"""

import _thread as thread, time

def counter(myId, count):
	for i in range(count):
		time.sleep(1)			#simulate real work
		mutex.acquire()			
		print('[%s] => %s'%(myId, i))		 
		mutex.release()

mutex = thread.allocate_lock()			# make a global lock object
for i in range(5):						# spawn 5 threads
	thread.start_new_thread(counter, (i,5))		# each thread loops 5 times

time.sleep(6)
print ('Main thread exiting.')