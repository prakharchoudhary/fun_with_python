import time
import webbrowser

i = 0
repeat = 3
while(i < repeat):
	time.sleep(1800)			#plays at an interval of 1800 secs or half an hour
	webbrowser.open("https://www.youtube.com/watch?v=Jm5DjptGtJo")
	i = i + 1
