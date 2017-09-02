"""
spawn threads to watch shared global memory change; threads normally exit
when the function they run returns, but _thread.exit() can be called to 
exit calling thread; _thread.exit is the same as sys.exit and raaising SYstemExit;;
thresds communnicate with possibly locked global vars; caveat: may need to make print/
input calls atomic on some platforms -- shared stdout;
"""

import _thread as thread
exitstat = 0

def child():
	global exitstat
	exitstat += 1
	threadid = thread.get_ident()
	print('Hello from child', threadid, exitstat)
	thread.exit()
	print('never reached')

def parent():
	while True:
		thread.start_new_thread(child, ())
		if input() == 'q':	break

if __name__ == '__main__':
	parent()


# CONCLUSION: since threads share global memory in common; the updated values of 
# `global exitstat` is returned.