#! python3
# A simple countdown script

import time, subprocess

timeLeft = 60
print("Timer for 60 seconds\n")
while timeLeft > 0:
	print(timeLeft, end='')
	time.sleep(1)
	timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)		# for windows