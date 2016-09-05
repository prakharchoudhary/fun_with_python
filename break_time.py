import os
import time
import webbrowser

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def timer(t):
	#t = t * 60
	time.sleep(t)			#plays at an interval of 1800 secs or half an hour
	webbrowser.open("https://www.youtube.com/watch?v=Jm5DjptGtJo")
	c = raw_input("Do you wish to restart the timer?[y/n]: ")
	if c=='y':
		print "-"*40 + "\n"
		t = int(raw_input("Set time(leave blank for 30 mins): "))
		timer(t)
	elif c == 'n':
		print "*"*40
		print "Awesome! You finished your work!"
		return

clear()
T = int(raw_input('Set the time(in mins) for your study interval: '))
timer(T)
