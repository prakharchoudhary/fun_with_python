import os
import sys
import time
import webbrowser
import datetime

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def time_elapsed(t):
	"""
	prints a progress bar of how much time has elapsed since the start.
	"""
	count = t
	interval = t // 60
	ticker = 1
	while(count):
		sys.stdout.write("\r [{}{}]: {}%".format("#"*(ticker), "-"*(60-ticker), (ticker*100)/60))
		sys.stdout.flush()
		count -= interval
		ticker += interval
		time.sleep(interval)
	print "\nCurrent time: " + datetime.datetime.now().strftime('%I:%M:%S %p')

def timer(t):
	t = t * 60
	print "\nYour timer starts at: " + datetime.datetime.now().strftime('%I:%M:%S %p') + "\n"
	# time.sleep(t)			#plays at an interval of 1800 secs or half an hour
	time_elapsed(t)
	# webbrowser.open_new("https://www.youtube.com/watch?v=2z8LGDzEX5k")
	c = raw_input("Do you wish to restart the timer?[y/n]: ")
	if c=='y':
		print "-"*40 + "\n"
		t = raw_input("Set time(leave blank for 30 mins): ")
		if t=='':
			t=30 
		timer(int(t))
	elif c == 'n':
		print "*"*40
		print "Awesome! You finished your work!"
		return

clear()
T = int(raw_input('Set the time(in mins) for your study interval: '))
timer(T)
