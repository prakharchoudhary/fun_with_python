import os
import urllib
import ast

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

name = None
clear()
while name != 'q':
	name = raw_input("Enter the name or press q to exit: ")

	def gender_check(x):
		key = "" #define key
		result = urllib.urlopen("https://gender-api.com/get?name={}&key={}".format(x, key))
		objects = result.read()
		real_obj = ast.literal_eval(objects)
		print real_obj['gender']
		result.close()
	
	if name != 'q':
		gender_check(name)

