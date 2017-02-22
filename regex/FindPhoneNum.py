import sys
import re

def findNum(string):
	phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
	# search = phoneNumRegex.search(string)		used to seach for the first occurence
	searchAll = phoneNumRegex.findall(string)
	# print('Phone number found: ' + searchAll.group())
	print(searchAll)

if __name__ == '__main__':
	string = input("Enter a string:\n")
	findNum(string)
